import unittest
import io
from contextlib import redirect_stdout
import os
from main import main


class TestMain(unittest.TestCase):
    def test_main(self):
        # check if the dataset file exists
        dataset_path = "Dataset-salary-2024.csv"
        self.assertTrue(
            os.path.exists(dataset_path), f"Dataset file {dataset_path} does not exist."
        )

        captured_output = io.StringIO()
        with redirect_stdout(captured_output):
            main()
        output = captured_output.getvalue()

        self.assertIn("Top 20 Job Titles Distribution:", output)
        self.assertIn("Experience Level Distribution:", output)
        self.assertIn("Salary Statistics by Experience Level:", output)

        # check if the markdown file exists
        markdown_file = "analysis_results.md"
        self.assertTrue(
            os.path.exists(markdown_file),
            f"Markdown file {markdown_file} was not generated.",
        )

        # check if the image files exist
        expected_images = [
            "output/salary_distribution.png",
            "output/job_title_distribution.png",
            "output/experience_level_distribution.png",
            "output/average_salary_by_job.png",
            "output/salary_vs_experience.png",
        ]
        for img_file in expected_images:
            self.assertTrue(
                os.path.exists(img_file), f"Image file {img_file} was not generated."
            )


if __name__ == "__main__":
    unittest.main()
