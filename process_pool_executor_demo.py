from concurrent.futures import ProcessPoolExecutor
import hashlib

texts = ["the quick brown fox jumped over the lazydog",
         "the big fat panda sat on the hungry snake",
         "the slick mountain lion ran up the tall tree"]


def generate_hash(text):
    return hashlib.sha384(str.encode(text, 'utf-8')).hexdigest()


if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        for text, hash_t in zip(texts, executor.map(generate_hash, texts)):
            print("\"%60s\" hash is %100s" % (text, hash_t))