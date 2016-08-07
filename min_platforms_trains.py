# Given two arrays containing arrival and departure times of trains from a station, find the min number of platforms
# required such that no train waits


def find_min_platforms(arrs, deps, N):
    if not arrs:
        return 0

    if len(arrs) == 1:
        return 1

    platforms_needed = 1
    result_max = 1

    i = 1; j = 0
    # Each arrival time (1 index ahead is compared to the departure time 1 index back)
    while i < N and j < N:
        if arrs[i] < deps[j]:
            platforms_needed += 1
            i += 1
            result_max = max(result_max, platforms_needed)
        else:
            platforms_needed -= 1
            j += 1

    return result_max


if __name__ == "__main__":
    arrs = map(lambda x: int(x), raw_input().split(" "))
    deps = map(lambda x: int(x), raw_input().split(" "))
    N = len(arrs)

    print "Min platforms needed: ", find_min_platforms(arrs, deps, N)