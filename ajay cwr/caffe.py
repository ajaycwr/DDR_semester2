product = {
    "americano": 37000,
    "caramel machiato": 59000,
    "asian dolce latte": 55000,
    "caramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappuccino": 48000,
    "caffe mocha": 55000,
}

def belanja():
    print("Selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp{harga} per kg") 
        
    total_belanja = 0
    while True:
        barang_dipilih = input("Masukkan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)").lower()
        if barang_dipilih.lower() == 'selesai':
             break
        if barang_dipilih not in product:
            print("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"Berapa kg {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total Belanja anda adalah: Rp{total_belanja}")
    
    ppn = total_belanja * 0.1
    print("Pajak: ", ppn)
    total_belanja += ppn

    

    if(total_belanja > 350000):
       diskon = total_belanja * 0.15
       total_belanja -= diskon

    

    print("total seluruh belanja anda adalah", total_belanja)
         
belanja()       
            