# Problem Index

Competitive programming problems organized by **pattern/technique**. Files follow the naming convention:

```
<platform>_<problem_id>_<short_description>.py
```

Platforms: `leetcode`, `codeforces`, `cses`, `atcoder`, `hackerrank`, `practice` (no specific platform).

---

## Folder Structure

| Pattern | Count | Description |
|---|---|---|
| `arrays/` | 11 | Array manipulation, simulation |
| `backtracking/` | 3 | Permutations, subset partitioning |
| `bfs-dfs/` | 5 | BFS, DFS, grid traversal |
| `binary-search/` | 5 | Binary search on values/answers |
| `dp/` | 6 | Dynamic programming |
| `dsu/` | 1 | Disjoint Set Union (Union-Find) |
| `graphs/` | 2 | Dijkstra, shortest paths |
| `greedy/` | 7 | Greedy algorithms |
| `hashing/` | 9 | Hashmaps, Counter, frequency tricks |
| `heap/` | 3 | Min/max heap, k-way merge |
| `intervals/` | 2 | Interval scheduling, sweep line |
| `math/` | 9 | Number theory, GCD, divisibility |
| `meet-in-middle/` | 1 | Split-and-merge search |
| `monotonic-stack/` | 1 | Monotonic stack patterns |
| `prefix-sum/` | 2 | Prefix/suffix sums, range queries |
| `recursion/` | 17 | Recursion fundamentals |
| `rolling-hash/` | 3 | Rolling hash, string hashing |
| `sliding-window/` | 1 | Sliding window technique |
| `sorting/` | 5 | Sorting algorithms, custom comparators |
| `two-pointers/` | 6 | Two-pointer technique |
| `learn/` | 20 | Python fundamentals (not problems) |

---

## Problem Table

| # | Problem | Platform | ID | Pattern | File |
|---|---------|----------|----|---------|------|
| 1 | Nutrients check | AtCoder | ABC356A | arrays | `arrays/atcoder_ABC356A_nutrients.py` |
| 2 | Subsegment reverse | AtCoder | ABC356B | arrays | `arrays/atcoder_ABC356B_subsegment_reverse.py` |
| 3 | Rotate buffer | Codeforces | 731A | arrays | `arrays/codeforces_731A_rotate_buffer.py` |
| 4 | New Year Chaos | HackerRank | — | arrays | `arrays/hackerrank_new_year_chaos.py` |
| 5 | Array manipulation | Practice | — | arrays | `arrays/practice_array_manipulation.py` |
| 6 | Good segments | Practice | — | arrays | `arrays/practice_good_segments.py` |
| 7 | Integer as array increment | Practice | — | arrays | `arrays/practice_integer_as_array_increment.py` |
| 8 | Lottery coupons | Practice | — | arrays | `arrays/practice_lottery_coupons.py` |
| 9 | Minimum swaps to sort | Practice | — | arrays | `arrays/practice_minimum_swaps_to_sort.py` |
| 10 | Remove min/max in min steps | Practice | — | arrays | `arrays/practice_remove_min_max_minimum_steps.py` |
| 11 | Reorder even numbers first | Practice | — | arrays | `arrays/practice_reorder_even_nums_first.py` |
| 12 | Unique Permutations II | LeetCode | 47 | backtracking | `backtracking/leetcode_47_unique_permutations.py` |
| 13 | Partition to K Equal Sum Subsets | LeetCode | 698 | backtracking | `backtracking/leetcode_698_partition_to_k_equal_subsets.py` |
| 14 | Generate permutations | Practice | — | backtracking | `backtracking/practice_generate_permutations.py` |
| 15 | Get neighbours in 2D matrix | Practice | — | bfs-dfs | `bfs-dfs/practice_get_neighbours_2d_matrix.py` |
| 16 | Number of Islands (BFS) | Practice | — | bfs-dfs | `bfs-dfs/practice_number_of_islands_bfs.py` |
| 17 | Path with min-max value (DFS TLE) | Practice | — | bfs-dfs | `bfs-dfs/practice_path_min_max_value_dfs_tle.py` |
| 18 | Paths to leaves with k consecutive 1s | Practice | — | bfs-dfs | `bfs-dfs/practice_paths_to_leaves_k_consecutive_ones.py` |
| 19 | Paths to leaves (TLE version) | Practice | — | bfs-dfs | `bfs-dfs/practice_paths_to_leaves_k_consecutive_ones_tle.py` |
| 20 | Count pairs with sum in range | Practice | — | binary-search | `binary-search/practice_count_pairs_sum_in_range.py` |
| 21 | Count strings smaller than self | Practice | — | binary-search | `binary-search/practice_count_strings_smaller_than_self.py` |
| 22 | Digit sum parities | Practice | — | binary-search | `binary-search/practice_digit_sum_parities.py` |
| 23 | Find missing number in AP | Practice | — | binary-search | `binary-search/practice_find_missing_number_in_ap.py` |
| 24 | Packing rectangles | Practice | — | binary-search | `binary-search/practice_packing_rectangles.py` |
| 25 | Dice Combinations | CSES | — | dp | `dp/cses_dice_combinations.py` |
| 26 | Dice Combinations (top-down) | CSES | — | dp | `dp/cses_dice_combinations_topdown.py` |
| 27 | Split Array With Same Average | LeetCode | 805 | dp | `dp/leetcode_805_split_array_same_average.py` |
| 28 | Fibonacci | Practice | — | dp | `dp/practice_fibonacci.py` |
| 29 | Fibonacci (bottom-up) | Practice | — | dp | `dp/practice_fibonacci_bottom_up.py` |
| 30 | Maximum Subarray Sum (Kadane) | Practice | — | dp | `dp/practice_maximum_subarray_sum_kadane.py` |
| 31 | Number of Islands (DSU) | Practice | — | dsu | `dsu/practice_number_of_islands_dsu.py` |
| 32 | Path With Minimum Effort | LeetCode | 1631 | graphs | `graphs/leetcode_1631_path_with_minimum_effort.py` |
| 33 | Path with min-max value (Dijkstra) | Practice | — | graphs | `graphs/practice_path_min_max_value_dijkstra.py` |
| 34 | Lax sorting binary string | Codeforces | 1969B | greedy | `greedy/codeforces_1969B_lax_sorting_binary_string.py` |
| 35 | Missing Coin Sum | CSES | — | greedy | `greedy/cses_missing_coin_sum.py` |
| 36 | Movie Festival | CSES | — | greedy | `greedy/cses_movie_festival.py` |
| 37 | Can reach end | Practice | — | greedy | `greedy/practice_can_reach_end.py` |
| 38 | Distribute candies equally | Practice | — | greedy | `greedy/practice_distribute_candies_equal.py` |
| 39 | Kayaking greedy | Practice | — | greedy | `greedy/practice_kayaking_greedy.py` |
| 40 | Take in increasing groups | Practice | — | greedy | `greedy/practice_take_in_increasing_groups.py` |
| 41 | Count pairs same difference | Codeforces | 1520D | hashing | `hashing/codeforces_1520D_count_pairs_same_difference.py` |
| 42 | Sum of Two Values | CSES | — | hashing | `hashing/cses_sum_of_two_values.py` |
| 43 | Find Common Characters | LeetCode | 1002 | hashing | `hashing/leetcode_1002_find_common_characters.py` |
| 44 | Max Points on a Line | LeetCode | 149 | hashing | `hashing/leetcode_149_max_points_on_a_line.py` |
| 45 | Longest Palindrome | LeetCode | 409 | hashing | `hashing/leetcode_409_longest_palindrome.py` |
| 46 | Can convert string | Practice | — | hashing | `hashing/practice_can_convert_string.py` |
| 47 | Count triplets forming GP | Practice | — | hashing | `hashing/practice_count_triplets_geometric_progression.py` |
| 48 | Hashable class / merge contacts | Practice | — | hashing | `hashing/practice_hashable_class_merge_contacts.py` |
| 49 | Recursive dict merge | Practice | — | hashing | `hashing/practice_recursive_dict_merge.py` |
| 50 | Merge sorted arrays (k-way) | Practice | — | heap | `heap/practice_merge_sorted_arrays.py` |
| 51 | Subsequence of K largest sum | Practice | — | heap | `heap/practice_subsequence_k_largest_sum.py` |
| 52 | Top-K longest strings from stream | Practice | — | heap | `heap/practice_top_k_longest_strings_stream.py` |
| 53 | Car Pooling | LeetCode | 1094 | intervals | `intervals/leetcode_1094_car_pooling.py` |
| 54 | Meeting Rooms II | LeetCode | 253 | intervals | `intervals/leetcode_253_meeting_rooms_2.py` |
| 55 | K-th Not Divisible | Codeforces | 1352C | math | `math/codeforces_1352C_k_th_not_divisible.py` |
| 56 | Divisibility by power of two | Codeforces | 1744D | math | `math/codeforces_1744D_divisibility_by_power_of_two.py` |
| 57 | Largest power of two in range | Codeforces | 1981A | math | `math/codeforces_1981A_largest_power_of_two.py` |
| 58 | Weird Algorithm (Collatz) | CSES | — | math | `math/cses_weird_algorithm.py` |
| 59 | Rotated Digits | LeetCode | 788 | math | `math/leetcode_788_rotated_digits.py` |
| 60 | Count subarrays with GCD = k | Practice | — | math | `math/practice_count_subarrays_with_gcd_k.py` |
| 61 | Divisibility rules | Practice | — | math | `math/practice_divisibility_rules.py` |
| 62 | Multiplying large numbers | Practice | — | math | `math/practice_multiplying_large_numbers.py` |
| 63 | Repdigit numbers | Practice | — | math | `math/practice_repdigit_numbers.py` |
| 64 | Closest Subsequence Sum | LeetCode | 1755 | meet-in-middle | `meet-in-middle/leetcode_1755_closest_subsequence_sum.py` |
| 65 | Nearest Smaller Values | CSES | — | monotonic-stack | `monotonic-stack/cses_nearest_smaller_values.py` |
| 66 | Find Pivot Index | LeetCode | 724 | prefix-sum | `prefix-sum/leetcode_724_find_pivot_index.py` |
| 67 | Subarray sum range query | Practice | — | prefix-sum | `prefix-sum/practice_subarray_sum_range_query.py` |
| 68 | Array average (recursive) | Practice | — | recursion | `recursion/practice_array_average.py` |
| 69 | Binary search (recursive) | Practice | — | recursion | `recursion/practice_binary_search_recursive.py` |
| 70 | Collatz 3n+1 | Practice | — | recursion | `recursion/practice_collatz_3n_plus_1.py` |
| 71 | Contest template | Practice | — | recursion | `recursion/practice_contest.py` |
| 72 | Convert to binary | Practice | — | recursion | `recursion/practice_convert_to_binary.py` |
| 73 | Creating expression | Practice | — | recursion | `recursion/practice_creating_expression.py` |
| 74 | Fast power | Practice | — | recursion | `recursion/practice_fast_power.py` |
| 75 | Knapsack (recursive) | Practice | — | recursion | `recursion/practice_knapsack.py` |
| 76 | Merge sort (recursive) | Practice | — | recursion | `recursion/practice_merge_sort_recursive.py` |
| 77 | Number of ways | Practice | — | recursion | `recursion/practice_number_of_ways.py` |
| 78 | Print digits | Practice | — | recursion | `recursion/practice_print_digits.py` |
| 79 | Print even indices | Practice | — | recursion | `recursion/practice_print_even_indices.py` |
| 80 | Pyramid | Practice | — | recursion | `recursion/practice_pyramid.py` |
| 81 | Reach value | Practice | — | recursion | `recursion/practice_reach_value.py` |
| 82 | Reverse string | Practice | — | recursion | `recursion/practice_reverse_string.py` |
| 83 | Suffix sum | Practice | — | recursion | `recursion/practice_suffix_sum.py` |
| 84 | Vowels | Practice | — | recursion | `recursion/practice_vowels.py` |
| 85 | Count duplicate strings | Practice | — | rolling-hash | `rolling-hash/practice_count_duplicate_strings.py` |
| 86 | Find non-overlapping strings | Practice | — | rolling-hash | `rolling-hash/practice_find_non_overlapping_strings.py` |
| 87 | Unique substrings same frequency | Practice | — | rolling-hash | `rolling-hash/practice_unique_substrings_same_frequency.py` |
| 88 | Count subarrays with target sum | Practice | — | sliding-window | `sliding-window/practice_count_subarrays_target_sum.py` |
| 89 | Stick Lengths | CSES | — | sorting | `sorting/cses_stick_lengths.py` |
| 90 | Custom sort | Practice | — | sorting | `sorting/practice_custom_sort.py` |
| 91 | Insertion sort | Practice | — | sorting | `sorting/practice_insertion_sort.py` |
| 92 | Merge sort | Practice | — | sorting | `sorting/practice_merge_sort.py` |
| 93 | Sort k increasing-decreasing | Practice | — | sorting | `sorting/practice_sort_k_increasing_decreasing.py` |
| 94 | Container With Most Water | LeetCode | 11 | two-pointers | `two-pointers/leetcode_11_container_with_most_water.py` |
| 95 | Strobogrammatic Number | LeetCode | 246 | two-pointers | `two-pointers/leetcode_246_strobogrammatic_number.py` |
| 96 | Append Characters to String | LeetCode | 2486 | two-pointers | `two-pointers/leetcode_2486_append_characters_to_string.py` |
| 97 | Count Pairs Less Than Target | LeetCode | 2824 | two-pointers | `two-pointers/leetcode_2824_count_pairs_less_than_target.py` |
| 98 | Sort Colors (Dutch National Flag) | LeetCode | 75 | two-pointers | `two-pointers/leetcode_75_sort_colors_dutch_national_flag.py` |
| 99 | Delete duplicates in sorted array | Practice | — | two-pointers | `two-pointers/practice_delete_duplicates_sorted_array.py` |

---

## Adding a New Problem

1. Identify the primary pattern/technique
2. Place the file in the corresponding folder
3. Name it: `<platform>_<id>_<short_description>.py`
4. Add a row to the table above
