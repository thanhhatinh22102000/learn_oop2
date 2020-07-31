from base import *

class TRA_CHANH(DO_UONG):
    def __init__(self,loai_coc,tt_shop,do_di_kem,loai_tra_chanh,topping_tra_chanh):
        self.loai_coc = loai_coc
        self.tt_shop = tt_shop
        self.do_di_kem = do_di_kem
        self.loai_tra_chanh=loai_tra_chanh
        self.topping_tra_chanh=topping_tra_chanh
    def tinh_tien(self):
        # 1:cốc to(20000 đ)/2:cốc nhỏ(15000 đ)
        # 1:có đồ đi kèm(5000 đ)/2:không có
        # 1:nha đam(2000 đ)/2:đào(3000 đ)/3:việt quất(4000 đ)/4:chanh(1000 đ)
        tong=0
        if self.loai_coc == 1:
            tong += 20000
        else:
            tong += 15000

        if self.do_di_kem == 1:
            tong += 5000
        else:
            pass

        if self.topping_tra_chanh==1:
            tong+=2000
        elif self.topping_tra_chanh==2:
            tong+=3000
        elif self.topping_tra_chanh==3:
            tong+=4000
        else:
            tong+=1000

        return tong
    def in_hoa_don(self):
        result=''
        result+='HÓA ĐƠN\ntên shop: '+str(self.tt_shop)+'\nloại cốc: '+str(self.loai_coc)+' /đồ đi kèm:  '+ str(self.do_di_kem)+' /loại trà:  '+str(self.loai_tra_chanh)+' /topping: '+str(self.topping_tra_chanh)+'\n-Thành Tiền: '+str(self.tinh_tien())+' đ'
        return result

if __name__=='__main__':
    tc=TRA_CHANH('','nhỏ','có','truyền thống','nha đam')
    print(tc.in_hoa_don())
    print(tc.tinh_tien())