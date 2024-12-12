from collections import defaultdict
from itertools import chain

def add_vecs(v1, v2):
    return v1[0]+v2[0], v1[1]+v2[1]

def subtract_vecs(v1, v2):
    return v1[0]-v2[0], v1[1]-v2[1]


class Cluster:
    def __init__(self, crop, tile):
        global clusters
        self.crop: str = crop
        self.id: int = len(clusters[crop])
        self.tiles: set = {tile}
        self.perimeter: int = 0

    def __repr__(self):
        return f"{self.crop} - {self.id}"

    def in_cluster(self, crop, tile):
        in_cluster = False
        if self.crop == crop:
            if tile not in self.tiles:
                for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nt = add_vecs(delta, tile)
                    if nt in self.tiles:
                        self.tiles.add(tile)
                        in_cluster = True
            else:
                in_cluster = True
        return in_cluster

    def recalc_perimeter(self):
        self.perimeter = 0
        for tile in self.tiles:
            this_perimeter = 0
            for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nt = add_vecs(delta, tile)
                if nt not in self.tiles:
                    this_perimeter += 1
            self.perimeter += this_perimeter

    def merge_cluster(self, other):
        is_merged = False
        if self.crop == other.crop and self.id != other.id:
            for t1 in self.tiles:
                for t2 in other.tiles:
                    if subtract_vecs(t1, t2) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        self.tiles.union(other.tiles)
                        is_merged = True
                        break
                    if is_merged:
                        break
                if is_merged:
                    break
        return is_merged



if __name__ == '__main__':
    in_file = open("../data/ex12.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    clusters = defaultdict(list)
    # clustered = set()

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]
            # if (i, j) in clustered:
            #     continue
            make_new_cluster = True
            for cluster in clusters[c]:
                if cluster.in_cluster(c, tile = (i, j)):
                    make_new_cluster = False
                    break
            if make_new_cluster:
                clusters[c].append(Cluster(c, (i, j)))
    ans_1 = 0


    for k, v in clusters.items():
        cluster_price = 0
        for cluster in v:
            cluster.recalc_perimeter()
            ans_1 += cluster.perimeter*len(cluster.tiles)
            print(cluster.crop, cluster.id, cluster.perimeter,len(cluster.tiles), cluster.perimeter*len(cluster.tiles))
    print(ans_1)





