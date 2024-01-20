import csv

def them_hoa_don(danh_sach_hd, so_hd, ngay_hd, ho_tenkh, dia_chi, quan, dien_thoai, tong_tien_hd, tam_ung, con_lai):
    danh_sach_hd.append({'so_hd':so_hd, 'ngay_hd':ngay_hd, 'ho_tenkh':ho_tenkh, 'dia_chi':dia_chi, 'quan':quan, 'dien_thoai':dien_thoai, 'tong_tien_hd':tong_tien_hd, 'tam_ung':tam_ung, 'con_lai':con_lai})

def in_ds_hoa_don(danh_sach_hd):
    for key in danh_sach_hd[0].keys():
        print(f'{key:<10}', end=' ')
    print()
    for entry in danh_sach_hd:
        for key in entry.keys():
            print(f'{entry[key]:<10}', end=' ')
        print()

def tra_cuu_hoa_don(danh_sach_hd, so_hd):
    hd_tuong_ung = []
    for hd in danh_sach_hd:
        if danh_sach_hd['so_hd'] == so_hd:
            hd_tuong_ung.append(hd)
    for key in hd_tuong_ung[0].keys():
        print(f'{key:<10}', end=' ')
    print()
    for entry in hd_tuong_ung:
        for key in entry.keys():
            print(f'{entry[key]:<10}', end=' ')
        print()

def xoa_hoa_don(danh_sach_hd, so_hd):
    da_xoa = False
    for i in danh_sach_hd:
        if i['so_hd'] == so_hd:
            danh_sach_hd.remove(i)
            da_xoa = True
            break
    if da_xoa:
        print("Đã xóa")

def thong_ke(danh_sach_hd):
    tong_tien = 0
    tong_tam_ung = 0
    tong_con_lai = 0
    for i in danh_sach_hd:
        tong_tien += i['tong_tien_hd']
        tong_tam_ung += i['tam_ung']
        tong_con_lai += i['con_lai']
    print(f"Tổng tất cả các hóa đơn: {tong_tien}")
    print(f"Tổng tạm ứng tất cả các hóa đơn: {tong_tam_ung}")
    print(f"Tổng còn lại tất cả các hóa đơn: {tong_con_lai} ")

def luu_file_csv(danh_sach_hd):
    with open("files/ds_hoadon.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=danh_sach_hd[0].keys)
        writer.writeheader
        writer.writerows(danh_sach_hd)
    print("Đã lưu")

def doc_file_csv():
    lstHoaDon = []
    with open("files/ds_hoadon.csv", mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            lstHoaDon.append(dict(row))
    print("Đã đọc file vào lstHoaDon")