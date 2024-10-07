"""
Core Service
"""
from sklearn.cluster import KMeans
import numpy as np
import spacy

nlp = spacy.load("en_core_web_md")

class RequirementEvaluator:
    """
    Class for Requirement Evaluation
    """
    def __init__(self, requirements):
        """
        Initialization with mapping requirement names to criteria sets
        :param requirements:
        """
        self.requirements = requirements

    def find_minimum_combination(self):
        """
        Find Minimum Combination
        :return:
        """
        uncovered_criteria = set()
        for criteria in self.requirements.values():
            uncovered_criteria.update(criteria)

        selected_requirements = set()

        while uncovered_criteria:
            best_requirement = None
            best_coverage = 0

            for req_name, criteria in self.requirements.items():
                coverage = len(criteria & uncovered_criteria)
                if coverage > best_coverage:
                    best_requirement = req_name
                    best_coverage = coverage

            if not best_requirement:
                raise ValueError("Some criteria cannot be covered by any requirement")

            selected_requirements.add(best_requirement)
            uncovered_criteria -= self.requirements[best_requirement]

        return selected_requirements

    def get_criteria_vectors(self, criteria_list):
        """
        get criteria Vector
        :param criteria_list:
        :return:
        """
        return np.array([nlp(criteria).vector for criteria in criteria_list])

    def cluster_criteria(self, criteria_list, n_clusters=3):
        """
        The cluster criteria
        :param criteria_list:
        :param n_clusters:
        :return:
        """
        vectors = self.get_criteria_vectors(criteria_list)
        k_means = KMeans(n_clusters=n_clusters, random_state=0).fit(vectors)
        return k_means.labels_, k_means.cluster_centers_

