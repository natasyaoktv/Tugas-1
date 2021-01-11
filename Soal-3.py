score1 = float(input("Masukkan nilai ujian praktek: "))
score2 = float(input("Masukkan nilai ujian teori: "))

if(score1>=70 and score2>=70):
    print("Selamat, anda lulus!")
elif(score1<70 and score2>=70):
    print("Anda harus mengulang ujian praktek.")
elif(score1>=70 and score2<70):
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori atau praktek.")