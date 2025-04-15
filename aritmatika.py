"""
Operasi Aritmatika

File ini berisi implementasi operasi-operasi aritmatika dasar dalam Python
dan demonstrasi penggunaannya.
"""


class Aritmatika:
    """Kelas untuk melakukan operasi aritmatika dasar."""
    
    @staticmethod
    def tambah(a, b):
        """Menambahkan dua angka."""
        return a + b
    
    @staticmethod
    def kurang(a, b):
        """Mengurangkan angka kedua dari angka pertama."""
        return a - b
    
    @staticmethod
    def kali(a, b):
        """Mengalikan dua angka."""
        return a * b
    
    @staticmethod
    def bagi(a, b):
        """Membagi angka pertama dengan angka kedua.
        
        Raises:
            ZeroDivisionError: Jika b adalah 0.
        """
        if b == 0:
            raise ZeroDivisionError("Pembagian dengan nol tidak diperbolehkan")
        return a / b
    
    @staticmethod
    def eksponen(a, b):
        """Menghitung a pangkat b."""
        return a ** b
    
    @staticmethod
    def modulus(a, b):
        """Menghitung sisa pembagian a oleh b.
        
        Raises:
            ZeroDivisionError: Jika b adalah 0.
        """
        if b == 0:
            raise ZeroDivisionError("Modulus dengan nol tidak diperbolehkan")
        return a % b
    
    @staticmethod
    def floor_division(a, b):
        """Menghitung pembagian bulat a oleh b.
        
        Raises:
            ZeroDivisionError: Jika b adalah 0.
        """
        if b == 0:
            raise ZeroDivisionError("Pembagian lantai dengan nol tidak diperbolehkan")
        return a // b
    
    @staticmethod
    def hitung_ekspresi_kompleks(x, y, z):
        """Menghitung ekspresi kompleks dengan prioritas operasi.
        
        Ekspresi: x ** y * z + x / y - y % z // x
        """
        try:
            hasil = x ** y * z + x / y - y % z // x
            return hasil
        except ZeroDivisionError:
            return "Error: Pembagian dengan nol dalam ekspresi"


def tampilkan_hasil(operasi, a, b, hasil, simbol):
    """Menampilkan hasil operasi aritmatika dengan format yang rapi."""
    print(f"{operasi}: {a} {simbol} {b} = {hasil}")


def demonstrasi_aritmatika():
    """Mendemonstrasikan penggunaan operasi aritmatika."""
    a = 10
    b = 3  # bisa pakai minus
    
    # Membuat objek aritmatika
    aritmatika = Aritmatika()
    
    # Demonstrasi operasi dasar
    print("\n=== OPERASI ARITMATIKA DASAR ===")
    tampilkan_hasil("Penjumlahan", a, b, aritmatika.tambah(a, b), "+")
    tampilkan_hasil("Pengurangan", a, b, aritmatika.kurang(a, b), "-")
    tampilkan_hasil("Perkalian", a, b, aritmatika.kali(a, b), "*")
    tampilkan_hasil("Pembagian", a, b, aritmatika.bagi(a, b), "/")
    tampilkan_hasil("Eksponen", a, b, aritmatika.eksponen(a, b), "**")
    tampilkan_hasil("Modulus", a, b, aritmatika.modulus(a, b), "%")
    tampilkan_hasil("Pembagian Lantai", a, b, aritmatika.floor_division(a, b), "//")
    
    print()  # Add an extra newline for separation
    
    # Demonstrasi ekspresi kompleks
    print("=== PRIORITAS OPERASI ===")
    x, y, z = 3, 2, 4
    ekspresi = "x ** y * z + x / y - y % z // x"  # Ensure this is on one line
    hasil = aritmatika.hitung_ekspresi_kompleks(x, y, z)
    print(f"Ekspresi: {ekspresi}")
    print(f"Dengan nilai x={x}, y={y}, z={z}")
    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    demonstrasi_aritmatika()
