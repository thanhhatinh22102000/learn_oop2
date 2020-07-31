import abc

class DO_UONG(abc.ABC):
    @abc.abstractclassmethod
    def __init__(self,loai_coc,tt_shop,do_di_kem):
        pass

    @abc.abstractclassmethod
    def tinh_tien(self):
        pass

    @abc.abstractclassmethod
    def in_hoa_don(self):
        pass