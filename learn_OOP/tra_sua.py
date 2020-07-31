from base import *

class TRA_SUA(DO_UONG):
    def __init__(self,tt_shop,loai_coc,do_di_kem,loai_sua,loai_tra,topping_tra_sua):
        self.loai_coc=loai_coc
        self.tt_shop=tt_shop
        self.do_di_kem=do_di_kem
        self.loai_sua=loai_sua
        self.loai_tra=loai_tra
        self.topping_tra_sua=topping_tra_sua
    def tinh_tien(self):
        # 1:cốc to(20000 đ)/2:cốc nhỏ(15000 đ)
        # 1:có đồ đi kèm(5000 đ)/2:không có
        # 1:trân châu(3000 đ)/2:thạch(4000 đ)/3:khoai môn(2000 đ)
        tong=0
        if self.loai_coc==1:
            tong+=20000
        else:
            tong+=15000

        if self.do_di_kem==1:
            tong+=5000
        else:
            pass

        if self.topping_tra_sua==1:
            tong+=3000
        elif self.topping_tra_sua==2:
            tong+=4000
        else:
            tong+=2000

        return tong
    def in_hoa_don(self):
        result = ''
        result +='HÓA ĐƠN\ntên shop: '+str(self.tt_shop) + '\nloại cốc: ' + str(self.loai_coc) + ' /đồ đi kèm:  ' + str(self.do_di_kem) + ' /loại sữa: ' + str(self.loai_sua) + ' /loại trà: ' + str(self.loai_tra)+' /topping: '+str(self.topping_tra_sua)+'\n-Thành Tiền: '+str(self.tinh_tien())+' đ'
        return result

if __name__=='__main__':
    ts=TRA_SUA('','to','có','sữa chua','tra xanh','trân châu trắng')
    print(ts.in_hoa_don())
    print(ts.tinh_tien())