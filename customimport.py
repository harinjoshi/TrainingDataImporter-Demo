from typing import Optional, Text, Dict, List, Union

import rasa
from rasa.core.domain import Domain
from rasa.core.interpreter import RegexInterpreter, NaturalLanguageInterpreter
from rasa.core.training.structures import StoryGraph
from rasa.importers.importer import TrainingDataImporter
from rasa.nlu.training_data import TrainingData


class ExcelImporter(TrainingDataImporter):
    """Example implementation of a custom importer component."""

    def __init__(self,training_data_paths:Text):
        """Constructor of your custom file importer.

        Args:
            config_file: Path to configuration file from command line arguments.
            domain_path: Path to domain file from command line arguments.
            training_data_paths: Path to training files from command line arguments.
            **kwargs: Extra parameters passed through configuration in configuration file.
        """
        pass

    
    async def get_nlu_data(self, language: Optional[Text] = "en") -> TrainingData:
        from rasa.nlu.training_data import loading

        path_to_nlu_file = self._custom_get_nlu_file()
        return loading.load_data(path_to_nlu_file)

    def _custom_get_nlu_file(self) -> Text:
        import os

        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, './BI_trainingdata.xlsx')
        print(file_path)
        return file_path