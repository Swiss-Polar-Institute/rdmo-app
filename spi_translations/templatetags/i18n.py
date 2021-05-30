from django.templatetags.i18n import *

register = Library()


def spi_language(text):
    text = text.replace('Catalog', 'Template')
    text = text.replace('catalog', 'template')

    text = text.replace('project', 'data management plan')
    text = text.replace('Project', 'Data management plan')

    return text


class SpiTranslateNode(TranslateNode):
    def render(self, context):
        result = super().render(context)

        result = spi_language(result)
        return result


class SpiBlockTranslateNode(BlockTranslateNode):
    def render(self, context, nested=False):
        result = super().render(context, nested)

        result = spi_language(result)
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


@register.tag("trans")
def spi_do_translate(parser, token):
    return do_translate(parser, token)


@register.tag("blocktrans")
def spi_do_block_translate(parser, token):
    return do_block_translate(parser, token)


@register.tag
def spi_language(parser, token):
    return language(parser, token)
