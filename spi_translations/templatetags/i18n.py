from django.templatetags.i18n import *

register = Library()

replacements = {'Catalog': 'Template',
                'catalog': 'template',
                'Project': 'Data management plan',
                'project': 'data management plan'
                }

do_not_replacements = ['Project RDMO', 'The project aims',
                       '?next=%2Fprojects%2Fjoin%2F']


def find_to_left(string, value, initial_position):
    while initial_position >= 0:
        if string[initial_position:initial_position+len(value)] == value:
            return initial_position

        initial_position -= 1

    return -1

def find_to_right(string, value, initial_position):
    while initial_position < len(string)-len(value):
        if string[initial_position:initial_position+len(value)] == value:
            return initial_position

        initial_position += 1

    return -1


def replace_if_in_text(text, original, destination):
    """
    Sometimes it can be in {$ .... $} angular. We do not want to replace
    it on this case.
    """
    position = 0
    while True:
        position = text.find(original, position)

        if position == -1:
            return text

        # If what's going to be replaced is between the angular escaping:
        # avoid replacing it
        left_curly_dollar = find_to_left(text, '{$', position)
        right_curly_dollar = find_to_right(text, '$}', position)

        if left_curly_dollar != -1 and right_curly_dollar != -1 and \
                left_curly_dollar < position < right_curly_dollar:
            # Advance without changing it
            position = right_curly_dollar
            continue

        to_replace = True
        for do_not_replace in do_not_replacements:
            start_do_not_replace = text.find(do_not_replace)

            if start_do_not_replace == -1:
                continue

            end_do_not_replace = start_do_not_replace + len(do_not_replace)

            if start_do_not_replace <= position <= end_do_not_replace:
                position = end_do_not_replace
                to_replace = False

        if to_replace:
            text = text[0:position] + destination + text[position+len(original):]


def translate_to_spi_language(text):
    if text == 'The project is funded by the German Research Foundation.':
        return text

    original_text = text

    for original, destination in replacements.items():
        text = replace_if_in_text(text, original, destination)

    return text


class SpiTranslateNode(TranslateNode):
    def render(self, context):
        result = super().render(context)

        result = translate_to_spi_language(result)
        return result


class SpiBlockTranslateNode(BlockTranslateNode):
    def render(self, context, nested=False):
        result = super().render(context, nested)

        result = translate_to_spi_language(result)
        return result


@register.tag("trans")
def spi_do_translate(parser, token):
    translated = do_translate(parser, token)
    return SpiTranslateNode(translated.filter_expression, translated.noop,
                            translated.asvar, translated.message_context)


@register.tag("blocktrans")
def spi_do_block_translate(parser, token):
    translated = do_block_translate(parser, token)
    return SpiBlockTranslateNode(translated.extra_context, translated.singular,
                                 translated.plural, translated.countervar,
                                 translated.counter, translated.message_context,
                                 translated.trimmed, translated.asvar)


@register.tag("translate")
def spi_do_translate(parser, token):
    translated = do_translate(parser, token)
    return SpiTranslateNode(translated.filter_expression, translated.noop,
                            translated.asvar, translated.message_context)


@register.tag("blocktranslate")
def spi_do_block_translate(parser, token):
    translated = do_block_translate(parser, token)
    return SpiBlockTranslateNode(translated.extra_context, translated.singular,
                                 translated.plural, translated.countervar,
                                 translated.counter, translated.message_context,
                                 translated.trimmed, translated.asvar)


@register.tag("get_available_languages")
def spi_do_get_available_languages(parser, token):
    return do_get_available_languages(parser, token)


@register.tag("get_language_info")
def spi_do_get_language_info(parser, token):
    return do_get_language_info(parser, token)


@register.tag("get_language_info_list")
def spi_do_get_language_info_list(parser, token):
    return do_get_language_info_list(parser, token)


@register.filter
def spi_language_name(lang_code):
    return language_name(lang_code)


@register.filter
def spi_language_name_translated(lang_code):
    return language_name_translated(lang_code)


@register.filter
def spi_language_name_local(lang_code):
    return language_name_local(lang_code)


@register.filter
def spi_language_bidi(lang_code):
    return language_bidi(lang_code)


@register.tag("get_current_language")
def spi_do_get_current_language(parser, token):
    return do_get_current_language(parser, token)


@register.tag("get_current_language_bidi")
def spi_do_get_current_language_bidi(parser, token):
    return do_get_current_language_bidi(parser, token)


@register.tag
def spi_language(parser, token):
    return language(parser, token)
