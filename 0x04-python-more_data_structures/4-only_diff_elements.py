#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1:
        if (set_2 is None):
            return set_1
        if set_2:
            s1 = list(set_1)
            s2 = list(set_2)
            s3 = []
            for i in range(0, len(s1)):
                s3.append(s1[i])
            for j in range(0, len(s2)):
                for l in range(0, len(s3)):
                    if s2[j] == s3[l]:
                        break
                    elif l < (len(s3) - 1):
                        continue
                    else:
                        s3.append(s2[j])
            return s3
    else:
        if set_2:
            return set_2
