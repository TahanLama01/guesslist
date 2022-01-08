import random

print("\n++++++++++++++++++++++++++++++++++++++++++++++")
kotak = [[1,2,3],
        [4,5,6],
        [7,8,9]]
for i in kotak:
    print(i)

nomor = ['Pertama','Kedua','Ketiga','Keempat','Kelima','Keenam','Ketujuh','Kedelapan','Kesembilan']
benar = 0
salah = 0

print("++++++++++++++++++++++++++++++++++++++++++++++")
nama =     input("Masukan Nama Anda  : ")
soal = int(input("Berapa soal [5/10] : "))
print("++++++++++++++++++++++++++++++++++++++++++++++\n")

if soal == 5 or soal == 10:
    for i in range(soal):
        acak = random.randrange(1,10)
        #print(acak)
        if acak == kotak[0][0]:
            print(f"{i+1}.Baris {nomor[0]} , Kolom {nomor[0]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        elif acak == kotak[0][1]:
            print(f"{i+1}.Baris {nomor[0]} , Kolom {nomor[1]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        elif acak == kotak[0][2]:
            print(f"{i+1}.Baris {nomor[0]} , Kolom {nomor[2]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        elif acak == kotak[1][0]:
            print(f"{i+1}.Baris {nomor[1]} , Kolom {nomor[0]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        elif acak == kotak[1][1]:
            print(f"{i+1}.Baris {nomor[1]} , Kolom {nomor[1]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        elif acak == kotak[1][2]:
            print(f"{i+1}.Baris {nomor[1]} , Kolom {nomor[2]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        elif acak == kotak[2][0]:
            print(f"{i+1}.Baris {nomor[2]} , Kolom {nomor[0]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        elif acak == kotak[2][1]:
            print(f"{i+1}.Baris {nomor[2]} , Kolom {nomor[1]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1      
        elif acak == kotak[2][2]:

            print(f"{i+1}.Baris {nomor[2]} , Kolom {nomor[2]} adalah")
            jawaban = int(input("Jawab : "))
            if jawaban == acak:
                print("Anda Benar")
                benar = benar + 1
            else:
                print("Anda Salah")
                print(f"Yang benar adalah : {acak}")
                salah = salah + 1
        else:
            print(f"Maaf, Tidak dapat mengerjakan Soal\nKarena No Random adalah : {acak}")
    if soal == 5:
        nilai = benar * 20
    elif soal == 10:
        nilai = benar * 10    

    data = {f'Nama  : {nama}\nSoal  : {soal}\nBenar : {benar}\nSalah : {salah}\nNilai : {nilai}'}

    print("\n+++++++++++++++++ Hasil ++++++++++++++++++++++")
    for i in data:
        print(i)
    print("++++++++++++++++++++++++++++++++++++++++++++++\n")

else:
    print("Pilih ulang! \n 5 atau 10 Soal")

