# Routh_Stability_Control_System_Assignment
 
Pada dasarnya program ini terdiri dari tiga fungsi utama: calculate_polynomial, create_routh_table, dan is_system_stable.

Fungsi calculate_polynomial digunakan untuk menghitung nilai polinomial untuk nilai s tertentu. Fungsi ini menerima dua parameter: koefisien polinomial dan nilai s. Fungsi ini menggunakan loop untuk menghitung nilai polinomial berdasarkan koefisien dan nilai s yang diberikan.

Fungsi create_routh_table digunakan untuk membuat tabel Routh untuk polinomial dan nilai K yang diberikan. Fungsi ini menerima dua parameter: koefisien polinomial dan nilai K. Fungsi ini membuat tabel Routh yang kosong dengan ukuran nxm, di mana n adalah jumlah koefisien polinomial dan m adalah n//2 (jika n ganjil) atau (n+1)//2 (jika n genap). Kemudian, fungsi mengisi dua baris pertama tabel Routh dengan koefisien yang diberikan dan menghitung baris-bari selanjutnya berdasarkan rumus Routh.

Fungsi is_system_stable digunakan untuk menentukan apakah sistem yang diwakili oleh tabel Routh dinyatakan stabil atau tidak stabil. Fungsi ini menerima tabel Routh sebagai parameter dan memeriksa apakah setiap elemen dalam kolom pertama tabel Routh bukan nol dan memiliki tanda yang sama. Jika semua elemen dalam kolom pertama tabel Routh bukan nol dan memiliki tanda yang sama, maka sistem dinyatakan stabil.

Selain tiga fungsi utama, kode program ini juga menunjukkan contoh penggunaan dari ketiga fungsi tersebut. Program ini menggunakan contoh polinomial 1s^3 + 6s^2 + 11s + 6 dan nilai K=2. Setelah tabel Routh dihitung, program menentukan apakah sistem dinyatakan stabil atau tidak stabil. Kemudian, program meminta pengguna untuk memasukkan nilai baru untuk K, menghitung tabel Routh untuk nilai K baru tersebut, dan menentukan apakah sistem dinyatakan stabil atau tidak stabil untuk nilai K baru tersebut.

Dengan program ini, pengguna dapat dengan mudah menghitung tabel Routh dan menentukan apakah sistem dinyatakan stabil atau tidak stabil dengan mudah. Selain itu, pengguna juga dapat mengubah nilai K dan melihat dampaknya pada stabilitas sistem.