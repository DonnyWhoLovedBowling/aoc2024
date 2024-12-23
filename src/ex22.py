from collections import defaultdict
from math import floor


def mix_and_prune(secret, number):
    # print(number)
    return (secret ^ number) % 16777216

def do_step(secret):
    secret = mix_and_prune(secret, (secret * 64))
    # print(secret)
    secret = mix_and_prune(secret, floor(secret / 32.) )
    # print(secret)
    secret = mix_and_prune(secret, secret * 2048)
    # print(secret)

    return secret


if __name__ == '__main__':
    in_file = open("../data/ex22.txt")
    secrets = [int(l.replace('\\n', '').strip()) for l in in_file.readlines()]
    # secrets = [123]
    sequences = defaultdict(list)
    price_map = dict()
    all_sequences = set()
    n = 10 if len(secrets) == 1 else 2000
    for step in range(n):
        for i in range(len(secrets)):
            if i not in price_map:
                price_map[i] = dict()

            s = secrets[i]
            price = int(str(s)[-1])
            new_secret = do_step(secrets[i])
            new_price = int(str(new_secret)[-1])
            secrets[i] = new_secret
            seq = sequences[i]
            seq.append(new_price-price)
            sequences[i] = seq[-4:]
            if len(seq) > 3:
                this_sq = tuple(seq[-4:])
                all_sequences.add(this_sq)
                if this_sq not in price_map[i]:
                    price_map[i][this_sq] = new_price

        if step % 100 == 0:
            print(step)
    print(sum(secrets))
    # print(all_sequences)
    # print(price_map)
    max_bananas = 0
    for seq in all_sequences:
        bananas = 0
        for i in range(len(secrets)):
            if seq in price_map[i]:
                bananas += price_map[i][seq]
        max_bananas = max(max_bananas, bananas)
    print(max_bananas)


