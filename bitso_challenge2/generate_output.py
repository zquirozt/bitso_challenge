import os


def generate_output_file(
    question: object, question_output: object, output_directory: object
) -> object:
    """

    :rtype: object
    """
    output_file = os.path.join(output_directory, f"{question}_result.csv")
    with open(output_file, "w") as file:
        file.write(str(question_output))
    print(f"{question}: Result saved to file {output_file}")
