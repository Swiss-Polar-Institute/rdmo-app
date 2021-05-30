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
