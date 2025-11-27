import csv
import io

from django.http import HttpResponse
from rdmo.projects.exports import Export
from rdmo.questions.models import Question


class SPICSVBase(Export):
    """
    Shared logic for custom CSV exports.
    """

    delimiter = ','

    def render(self):
        project = self.project
        queryset = project.values.filter(snapshot=None).order_by(
            'set_prefix', 'set_index', 'collection_index'
        )

        # Prepare CSV
        output = io.StringIO()
        writer = csv.writer(output, delimiter=self.delimiter)

        # Header row
        writer.writerow(["Section", "Question Set", "Question", "Answer"])

        # Questions sorted by catalog order
        questions = Question.objects.order_by_catalog(project.catalog)

        for q in questions:
            section_title = q.questionset.section.title if q.questionset.section else ""
            qs_title = q.questionset.title if q.questionset else ""

            values = queryset.filter(attribute=q.attribute)

            if not values.exists():
                writer.writerow([section_title, qs_title, q.text, ""])
            else:
                for v in values:
                    answer_text = v.text if v.text else v.value if v.value else ""
                    writer.writerow([section_title, qs_title, q.text, answer_text])

        # Build downloadable response
        csv_data = output.getvalue()
        response = HttpResponse(csv_data, content_type="text/csv")
        response['Content-Disposition'] = f'attachment; filename="{project.title}.csv"'
        return response


class SPICSVCommaExport(SPICSVBase):
    delimiter = ','


class SPICSVSemicolonExport(SPICSVBase):
    delimiter = ';'
