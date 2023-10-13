from enums import JobKeyword


def get_job_key_words_from_string(job_title: str) -> list[JobKeyword]:
    strings_to_parse = job_title.upper().split()
    job_keywords = []
    valid_keywords = JobKeyword.list_values()
    for word in strings_to_parse:
        if word in valid_keywords:
            job_keywords.append(JobKeyword[word])
    return job_keywords
