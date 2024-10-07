"""
Application EvaluationService Module
"""
import json
import os
from collections import defaultdict

import pandas as pd

from domain.services import RequirementEvaluator


class EvaluationService:
    """
    Class Evaluation Service
    """
    def __init__(self, filename, filepath):
        """
        Initialise Evaluation Service
        :param filename:
        """
        self.filename = filename
        self.filepath = filepath
        print(self.filename, "Filename here", self.filepath, "path here")
        self.requirements = self.load_requirements()

    def load_requirements(self):
        """
        Load requirements and their corresponding evaluation criteria from a CSV file.
        """
        df = pd.read_csv(self.filepath)
        requirement_to_criteria = defaultdict(set)
        for _, row in df.iterrows():
            requirement = row.get('Requirement', None)
            if requirement is not None:
                criteria_list = {c.strip().lower() for c in row.get('Evaluation Criteria').split(',')}
                requirement_to_criteria[requirement].update(criteria_list)

        return requirement_to_criteria

    def evaluate(self):
        evaluator = RequirementEvaluator(self.requirements)
        return evaluator.find_minimum_combination()

    def output_results(self, selected_requirements, output_filename='minimum_combination_output.csv',
                       output_as_json=False):
        """
        Output the results to a CSV file or return JSON data based on the output_as_json parameter.

        :param selected_requirements: The selected requirements for evaluation.
        :param output_filename: The name of the output file (for CSV).
        :param output_as_json: If True, return the output as JSON instead of saving it to a file.
        :return: The full path of the saved CSV file if output_as_json is False, else JSON data.
        """
        output_data = []
        for req in selected_requirements:
            output_data.append({
                'Requirement': req,
                'Minimum Evaluation Criteria': ', '.join(self.requirements[req])
            })

        # If output_as_json is True, return the JSON representation
        if output_as_json:
            return json.dumps(output_data, indent=4)

        # Construct the full path for the output file
        output_directory = os.path.dirname(
            os.path.abspath(self.filename))  # Save in the same directory as the input file
        full_output_path = os.path.join(output_directory, output_filename)

        # Save the DataFrame to the specified output path
        df = pd.DataFrame(output_data)
        df.to_csv(full_output_path, index=False)

        return full_output_path