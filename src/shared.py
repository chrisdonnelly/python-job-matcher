from enums import JobKeyword


def get_job_keywords(string: str) -> list[JobKeyword]:
    strings_to_parse = string.upper().split()
    job_key_words = [
        getattr(JobKeyword, word, None)
        for word in strings_to_parse
        if word in JobKeyword.list_values()
    ]
    return job_key_words
