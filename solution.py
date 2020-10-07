def solution(s):

    string_len = len(s)
    max_count = 0
    # where to start cutting a cake
    first_cut_from = 0
    # restrictions, without which the problem makes no sense
    min_sample_len = 3
    max_sample_len = string_len // 2

    for i in range(string_len):
        for j in range(max_sample_len - min_sample_len + 1):
            up_to = i+j+min_sample_len
            if up_to <= string_len:
                sample = s[i:up_to]
                first_cut_from = i
                sample_len = len(sample)
            else:
                break
            found_index = i
            count = 1
            while True:
                if found_index + sample_len < string_len:
                    found_index = s.find(sample, found_index + sample_len)
                    if found_index != -1:
                        count += 1
                    else:
                        # But the cake is "looped" and we don't know
                        # where to start cutting
                        if i != 0:
                            end = s[string_len-sample_len+1:]
                            if i > sample_len:
                                start = s[:sample_len-1]
                            else:
                                start = s[:first_cut_from]
                            joint = end + start
                            if joint.find(sample) != -1:
                                count += 1
                        if count > max_count:
                            max_count = count
                        break
                else:
                    break
    return max_count
