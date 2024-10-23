def solution(data, target_ext, target_value, sort_by):
    result = []
    headers = ["code", "date", "maximum", "remain"]
    ext_index = headers.index(target_ext)

    for row in data:
        if row[ext_index] < target_value:
            result.append(row)

    sorted_result = sorted(result, key=lambda x: x[headers.index(sort_by)])
    return sorted_result
