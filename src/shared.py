from enums import JobTitleKeyword


def get_job_key_words_from_string(string: str) -> list[JobTitleKeyword]:
    string_to_upper = string.upper()
    strings_to_parse = string_to_upper.split()
    job_keywords = []
    valid_keywords = JobTitleKeyword.list_values()
    for word in strings_to_parse:
        if word in valid_keywords:
            job_keywords.append(JobTitleKeyword[word])
    return job_keywords
