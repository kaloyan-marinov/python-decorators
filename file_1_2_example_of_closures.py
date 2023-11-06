import pprint
from typing import List, Dict, Optional


class RequestHandlingFacilitator:
    def __init__(self, mock_examples: List[Dict]):
        # Perform validation.
        for i, mock_example_i in enumerate(mock_examples):
            if mock_example_i["id"] != i + 1:
                raise ValueError(
                    f"The value stored in 'mock_examples[{i}]` must be {i + 1}"
                    f" but instead found {mock_examples[i]['id']}"
                )

        self._mock_examples = mock_examples

    def create_mock_fetch_examples(self):
        def mock_fetch_examples() -> List[Dict]:
            return self._mock_examples

        return mock_fetch_examples

    def create_mock_create_example(self):
        def mock_create_example(
            source_language: str,
            new_word: str,
            content: Optional[str],
            content_translation: Optional[str],
        ) -> Dict:
            # The following way of generating an ID for the new (mock) example
            # is guaranteed to be reasonable/meaningful
            # thanks to the validation performed above.
            id_for_new_example = len(self._mock_examples) + 1

            new_example = {
                "id": id_for_new_example,
                "source_language": source_language,
                "new_word": new_word,
                "content": content,
                "content_translation": content_translation,
            }

            self._mock_examples.append(new_example)

            return new_example

        return mock_create_example


def main():
    mock_examples = [
        {
            "id": index + 1,
            "source_language": "Finnish",
            "new_word": f"sana numero-{index + 1}",
            "content": f"esimerkki sanalla numero-{index + 1}",
            "content_translation": f"example with word number-{index + 1}",
        }
        for index in range(3)
    ]

    r_h_f = RequestHandlingFacilitator(mock_examples)
    mock_fetch_examples = r_h_f.create_mock_fetch_examples()
    mock_create_example = r_h_f.create_mock_create_example()

    pretty_printer = pprint.PrettyPrinter(indent=4)

    # The mock response generated in the next statement
    # contains the 3 hard-coded examples.
    mock_response_1 = mock_fetch_examples()
    print()
    pretty_printer.pprint(mock_response_1)

    # The mock response generated in the next statement
    # is equal to
    #   ```
    #   {
    #       "content": "Aurinko paistaa.",
    #       "content_translation": "The sun is shining.",
    #       "id": 4,
    #       "new_word": "aurinko",
    #       "source_language": "Finnish",
    #   }
    #   ```
    mock_response_2 = mock_create_example(
        "Finnish",
        "aurinko",
        "Aurinko paistaa.",
        "The sun is shining.",
    )
    print()
    pretty_printer.pprint(mock_response_2)

    # The mock response generated in the next statement
    # contains all of the (3 + 1) examples that were mentioned above.
    mock_response_3 = mock_fetch_examples()
    print()
    pretty_printer.pprint(mock_response_3)


if __name__ == "__main__":
    main()
