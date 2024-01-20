import libs.xu_ly_hoa_don

danh_sach_hd = []
lua_chon = int(input("""CHƯƠNG TRÌNH QUẢN LÝ HÓA ĐƠN
                    1: Thêm hóa đơn
                    2: Danh sách hóa đơn
                    3: Tra cứu hóa đơn
                    4: Xóa hóa đơn
                    5: Thống kê
                    6: Lưu danh sách hóa đơn ra file CSV
                    7: Đọc file CSV
                    Chọn chức năng cần thực hiện: """))

if lua_chon == 1:
    while True:
        print("Nhập thông tin hóa đơn:")
        so_hd = input("So hoa don: ")
        ngay_hd = input("Ngay hoa don: ")
        ho_tenkh = input("Ho ten khach hang: ")
        dia_chi = input("Dia chi: ")
        quan = input("Quan: ")
        dien_thoai = input("Dien thoai: ")
        tong_tien_hd = int(input("Tong tien hoa don: "))
        tam_ung = int(input("Tam ung: "))
        libs.xu_ly_hoa_don.them_hoa_don(danh_sach_hd, so_hd, ngay_hd, ho_tenkh, dia_chi, quan, dien_thoai, tong_tien_hd, tam_ung, (tong_tien_hd-tam_ung))
        tiep_tuc = input("Ban co muon tiep tuc (1:TT): ")
        if tiep_tuc != "1":
            break

elif lua_chon == 2:
    libs.xu_ly_hoa_don.in_ds_hoa_don(danh_sach_hd)

elif lua_chon == 3:
    so_hd = input("Cho biết số hóa đơn: ")
    libs.xu_ly_hoa_don.tra_cuu_hoa_don(danh_sach_hd, so_hd)

elif lua_chon == 4:
    so_hd = input("Cho biết số hóa đơn: ")
    libs.xu_ly_hoa_don.xoa_hoa_don(danh_sach_hd, so_hd)

elif lua_chon == 5:
    libs.xu_ly_hoa_don.thong_ke(danh_sach_hd)

elif lua_chon == 6:
    libs.xu_ly_hoa_don.luu_file_csv(danh_sach_hd)

elif lua_chon == 7:
    libs.xu_ly_hoa_don.doc_file_csv()