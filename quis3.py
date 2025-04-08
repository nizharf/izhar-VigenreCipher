import string

plaintext = """
Di sebuah taman kota, angin sore bertiup lembut, menggoyangkan dedaunan yang mulai
menguning. Beberapa orang duduk di bangku taman, menikmati suasana yang tenang setelah
seharian bekerja. Anak-anak berlarian di area bermain, tertawa riang saat bermain ayunan dan
perosotan. Seorang penjual es krim melintas, menawarkan dagangannya kepada pengunjung
yang bersantai. Di sudut taman, seorang pria tua membaca buku dengan tenang, sesekali
tersenyum menikmati cerita yang ia baca. Burung-burung kecil berkicau di dahan pohon,
menambah harmoni suasana sore. Matahari perlahan mulai tenggelam, meninggalkan cahaya
keemasan di langit yang semakin temaram. Lampu-lampu taman mulai menyala, menerangi jalur
setapak yang dipenuhi pejalan kaki.
"""

key = "NIZHARFAKHZIAR"
def clean_text(text):
    text = text.upper()
    allowed = set(string.ascii_uppercase)
    return ''.join([c for c in text if c in allowed])

def text_to_numbers(text):
    return [ord(c) - ord('A') for c in text]

def numbers_to_text(numbers):
    return ''.join([chr(n + ord('A')) for n in numbers])

def extend_key(key, length):
    key = clean_text(key)
    return (key * (length // len(key) + 1))[:length]

def vigenere_encrypt(plaintext, key):
    plaintext = clean_text(plaintext)
    extended_key = extend_key(key, len(plaintext))
    plaintext_nums = text_to_numbers(plaintext)
    key_nums = text_to_numbers(extended_key)
    cipher_nums = [(p + k) % 26 for p, k in zip(plaintext_nums, key_nums)]
    return numbers_to_text(cipher_nums)

if __name__ == "__main__":
    result = vigenere_encrypt(plaintext, key)
    print("Hasil Enkripsi:", result)