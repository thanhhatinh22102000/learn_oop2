from tra_sua import *
from tra_chanh import *

if __name__=='__main__':
    tt=1
    LIST=[]
    print('Mời quý khách order!\n')
    while tt==1:
        tt_shop=input('Nhập tt shop:\t')
        loai_coc=eval(input('Chọn loại cốc(1:cốc to/2:côc nhỏ):\t'))
        do_di_kem=eval(input('Bạn có muốn đồ đi kèm không?(1:có/2:không):\t'))
        loai_do_uong=eval(input('Bạn muốn uống gì?(1:trà sữa/2:trà chanh):\t'))
        if loai_do_uong==1:
            loai_sua=input('Chọn loai sữa(sữa chua/sữa tươi/sữa bò):\t')
            loai_tra=input('Chọn loại trà(trà xanh/trà vàng/trà thảo mộc):\t')
            topping_tra_sua=eval(input('Chọn topping(1:trân châu/2:thạch/3:khoai môn):\t'))
        else:
            loai_tra_chanh=input('Chọn trà chanh(truyền thống,kết hợp,pha chế):\t')
            topping_tra_chanh=eval(input('Chọn topping(1:nha đam/2:đào/3:việt quất/4:chanh):\t'))

        if loai_do_uong==1:
            L=TRA_SUA(tt_shop,loai_coc,do_di_kem,loai_sua,loai_tra,topping_tra_sua)
        else:
            L=TRA_CHANH(loai_coc,tt_shop,do_di_kem,loai_tra_chanh,topping_tra_chanh)

        LIST.append(L)

        tt=eval(input('Bạn muốn order nữa không?(1:có/2:không): '))

    for i in LIST:
        print(i.in_hoa_don())