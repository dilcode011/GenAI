from langchain.prompts.example_selector import LengthBasedExampleSelector

selector = LengthBasedExampleSelector(
    examples=[
        {"input": "short", "output": "ok"},
        {"input": "long example text", "output": "fine"}
    ],
    max_length=10
)