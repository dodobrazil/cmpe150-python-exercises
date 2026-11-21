# variable
input_arguments = [[
    ["Z", "C", "M", "Z", "Z", "B", "A", "P1"],
    ["M", "Z", "Z", "P", "E", "Z", "Z", "Z"],
    ["P", "Z", "Z", "Z", "Z", "Z", "Z", "Z"],
    ["Z", "E", "Z", "Z", "Z", "P", "Z", "Z"],
    ["Z", "Z", "Z", "Z", "Z", "Z", "I", "Z"],
    ["Z", "Z", "B", "A", "0", "Z", "3", "L"],
    ["Z", "Z", "Z", "Z", "Z", "Z", "Z", "P1"],
    ["Z", "Z", "Z", "Z", "Z", "Z", "Z", "Z"]
], ['CMPE', 'PILAB']]
# variable

# assign your result to this variable
output_dictionary = None

# DO NOT CHANGE THE CODE ABOVE

# Modify this function for your solution
def decode_grid(grid, possible_words):

    portals_dict = {}

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val.startswith('P') and len(val) > 1 and val[1:].isdigit():
                if val not in portals_dict:
                    portals_dict[val] = []
                portals_dict[val].append((i, j))
#özel karakter bulucular
    def inside_grid(r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])

    def is_wall(ch):
        return ch == '0'

    def is_joker(ch):
        return ch == '#'

    def is_star(ch):
        return ch == '*'

    def is_portal(ch):
        return (ch in portals_dict) and (len(portals_dict[ch]) == 2)

    def is_jump_cell(ch):
        return ch.isdigit()

    def is_letter(ch):
        return ch.isalpha()

    #zıplarken engel?
    
    def can_jump_path(i1, j1, i2, j2):

        di = 0 if i1 == i2 else (1 if i2 > i1 else -1)
        dj = 0 if j1 == j2 else (1 if j2 > j1 else -1)

        def check_cells(r, c):
            if r == i2 and c == j2:
                return not is_wall(grid[r][c])
            if is_wall(grid[r][c]):
                return False
            return check_cells(r + di, c + dj)

        # ilk adım (i1+di, j1+dj)başlayarak i2,j2'ye kadar bakmacaa
        return check_cells(i1 + di, j1 + dj)

    def get_neighbors(i, j, step):

        directions = [(-1, -1), (-1, 0), (-1, 1),
                      ( 0, -1),          ( 0, 1),
                      ( 1, -1), ( 1, 0), ( 1, 1)]

        def collect_dirs(dir_list):
            if not dir_list:
                return []
            (dx, dy) = dir_list[0]
            rest = dir_list[1:]
            nx, ny = i + dx*step, j + dy*step
            if inside_grid(nx, ny) and can_jump_path(i, j, nx, ny):
                return [(nx, ny)] + collect_dirs(rest)
            else:
                return collect_dirs(rest)

        return collect_dirs(directions)

    def dfs(i, j, word, index, visited, path, step):

        if index == len(word):
            return [path[:]]  # path kopyası

        if not inside_grid(i, j) or (i, j) in visited:
            return []

        cell_val = grid[i][j]
        
        if is_wall(cell_val):
            return []

        new_index = index
        if is_joker(cell_val):
            new_index = index + 1
        elif is_star(cell_val):
            pass
        elif is_portal(cell_val):
            pass
        elif is_jump_cell(cell_val):
            pass
        else:
            # normal harf
            if is_letter(cell_val) and cell_val == word[index]:
                new_index = index + 1
            else:
                return []

        #hücreyi path'e eklemece
        path.append((i, j))
        visited.add((i, j))

        #zıplama
        new_step = step
        if is_jump_cell(cell_val):
            jump_factor = int(cell_val)
            new_step = step * jump_factor
        else:
            # Portal, yıldız, joker, normal harf vb. step 1
            new_step = 1

        # Komşu
        next_cells = get_neighbors(i, j, new_step)

        #
        if is_portal(cell_val):
            # portals_dict[cell_val] --- [(x1,y1), (x2,y2)]
            plist = portals_dict[cell_val]
            if len(plist) == 2:
                (p1, p2) = plist

                other_portal = p1 if (p2 == (i,j)) else p2
                next_cells.append(other_portal)

        results = []

        def explore_all(ncells):
            if not ncells:
                return
            (nx, ny) = ncells[0]
            tail = ncells[1:]
            found_paths = dfs(nx, ny, word, new_index, visited, path, new_step)
            for fp in found_paths:
                results.append(fp)
            explore_all(tail)

        explore_all(next_cells)

        # Geri dönüş (backtrack)
        path.pop()
        visited.remove((i, j))

        return results

    
    def path_length_euclid(pth):
        """
        pth = [(i1,j1), (i2,j2), ...]
        Düz hareket = 1, diyagonal = sqrt(2).
        Jump ise aradaki mesafeye göre (örn 2 düz => 2, 2 diyagonal => 2*sqrt(2)).
        """
        dist = 0.0
        for idx in range(len(pth)-1):
            (r1,c1) = pth[idx]
            (r2,c2) = pth[idx+1]
            dr, dc = abs(r2 - r1), abs(c2 - c1)
            if dr == dc:
                # diagonal
                dist += dr * ((2)**0.5)
            else:
                # düz
                dist += (dr + dc)
        return dist

    def dist_to_top_left(r, c):
        # (0,0)a uzaklık
        return ((r - 0)**2 + (c - 0)**2)**0.5

    def dist_to_bottom_right(r, c):
        # (maxRow, maxCol) uzaklık
        rr = len(grid) - 1
        cc = len(grid[0]) - 1
        return ((rr - r)**2 + (cc - c)**2)**0.5

    def sort_paths(pth_list):
        def sort_key(p):
            #uzunluk 
            plen = path_length_euclid(p)
            #start top-left
            (sr, sc) = p[0]
            start_dist = dist_to_top_left(sr, sc)
            # 3)end bottom-right
            (er, ec) = p[-1]
            end_dist = dist_to_bottom_right(er, ec)
            return (plen, start_dist, end_dist)
        return sorted(pth_list, key=sort_key)

    found_dict = {}
    # Döngü1
    for w in possible_words:
        all_paths_for_this_word = []
        # Döngü2
        for i in range(len(grid)):
            # Döngü3
            for j in range(len(grid[0])):
                found_paths = dfs(i, j, w, 0, set(), [], 1)
                all_paths_for_this_word.extend(found_paths)

        unique_paths_set = set(tuple(p) for p in all_paths_for_this_word)
        unique_paths_list = [list(path_tuple) for path_tuple in unique_paths_set]

        # Sıralama
        if unique_paths_list:
            unique_paths_list = sort_paths(unique_paths_list)
            found_dict[w] = unique_paths_list

    return found_dict

# DO NOT CHANGE THE CODE BELOW
output_dictionary = decode_grid(input_arguments[0], input_arguments[1])