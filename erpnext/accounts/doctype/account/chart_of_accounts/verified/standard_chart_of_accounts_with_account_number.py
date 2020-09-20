# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
from frappe import _

def get():
    return {
        "Aktiva": {
            "Aktiva Lancar": {
                "Akun sementara": {
                    "Pembukaan sementara": {
                        "account_number": "1170.001", 
                        "account_type": "Temporary"
                    }, 
                    "account_number": "1170.000"
                }, 
                "Bank ": {
                    "Rekening Bank": {
                        "account_number": "1121.001",
                        "account_type": "Bank"
                    }, 
                    "account_number": "1120.000",
                    "is_group": 1
                }, 
                "Biaya Bayar Dimuka": {
                    "Biaya Bayar Dimuka": {
                        "account_number": "1150.001"
                    }, 
                    "account_number": "1150.000"
                }, 
                "Kas": {
                    "Kas Besar": {
                        "account_number": "1112.001", 
                        "account_type": "Cash"
                    }, 
                    "Kas Kecil": {
                        "account_number": "1111.001", 
                        "account_type": "Cash"
                    }, 
                    "account_number": "1110.000"
                }, 
                "Pendapatan Yang Akan Diterima": {
                    "Pendapatan Yang Akan Diterima": {
                        "account_number": "1160.001"
                    }, 
                    "account_number": "1160.000"
                }, 
                "Persediaan Barang": {
                    "Persediaan Barang": {
                        "account_number": "1141.001", 
                        "account_type": "Stock"
                    }, 
                    "Uang Muka Pembelian": {
                        "account_number": "1142.001", 
                        "account_type": "Bank"
                    }, 
                    "account_number": "1140.000"
                }, 
                "Piutang": {
                    "Piutang Dagang": {
                        "account_number": "1131.001", 
                        "account_type": "Receivable"
                    }, 
                    "Piutang Karyawan": {
                        "account_number": "1132.001", 
                        "account_type": "Receivable"
                    }, 
                    "Piutang Lain-lain": {
                        "account_number": "1133.001", 
                        "account_type": "Receivable"
                    }, 
                    "account_number": "1130.000"
                }, 
                "account_number": "1100.000"
            }, 
            "Aktiva Tetap": {
                "Aset": {
                    "Bangunan": {
                        "account_number": "1211.001", 
                        "account_type": "Fixed Asset"
                    }, 
                    "Kendaraan": {
                        "account_number": "1212.001", 
                        "account_type": "Fixed Asset"
                    }, 
                    "Mesin & Peralatan": {
                        "account_number": "1213.001", 
                        "account_type": "Fixed Asset"
                    },
                    "account_number": "1210.000"
                },
                "Akumulasi Penyusutan Aset": {
                    "Akumulasi Penyusutan Aset": {
                        "account_number": "1220.001", 
                        "account_type": "Accumulated Depreciation"
                    }, 
                    "account_number": "1220.000"
                }, 
                "Investasi": {
                    "Deposito": {
                        "account_number": "1231.001"
                    }, 
                    "Investasi Surat Berharga": {
                        "account_number": "1232.001"
                    }, 
                    "Investasi Properti": {
                        "account_number": "1233.001"
                    }, 
                    "account_number": "1230.000"
                }, 
                "Aktiva Tetap Lainnya": {
                    "Biaya Ditangguhkan": {
                        "account_number": "1251.001"
                    }, 
                    "account_number": "1250.000"
                }, 
                "account_number": "1200.000"
            }, 
            "account_number": "1000.000", 
            "root_type": "Asset"
        }, 
        "Pengeluaran": {
            "Beban Lain-lain": {
                "Beban Lain-lain": {
                    "Beban Administrasi Bank": {
                        "account_number": "5510.001"
                    }, 
                    "Beban Bunga Kredit Rekening Koran Bank": {
                        "account_number": "5510.004"
                    }, 
                    "Beban Bunga Pinjaman Pada Pihak Ketiga": {
                        "account_number": "5510.005"
                    }, 
                    "Beban Notaris Dan Administrasi Kredit Bank": {
                        "account_number": "5510.003"
                    }, 
                    "Beban Pajak Bumi & Bangunan": {
                        "account_number": "5510.006",
                        "account_type": "Tax"
                    },
                    "Beban Pajak PPN": {
                        "account_number": "5510.008",
                        "account_type": "Tax" 
                    }, 
                    "Beban Pajak Penghasilan ": {
                        "account_number": "5510.007",
                        "account_type": "Tax" 
                    }, 
                    "Beban Provisi Pinjaman Bank": {
                        "account_number": "5510.002"
                    }, 
                    "Selisih Kurs": {
                        "account_number": "5510.010", 
                        "account_type": "Round Off"
                    }, 
                    "Selisih Pembayaran Pembeli": {
                        "account_number": "5510.009", 
                        "account_type": "Round Off"
                    }, 
                    "account_number": "5510.000"
                }, 
                "account_number": "5500.000"
            }, 
            "Beban Langsung": {
                "Beban Penjualan": {
                    "Biaya Asuransi Kendaraan Operasional": {
                        "account_number": "5110.009"
                    }, 
                    "Biaya BBM": {
                        "account_number": "5110.001"
                    }, 
                    "Biaya Barang Rusak": {
                        "account_number": "5110.007"
                    }, 
                    "Biaya Bonus, Hadiah, dan Sampel": {
                        "account_number": "5110.012"
                    }, 
                    "Biaya Entertainment dan Pergaulan": {
                        "account_number": "5110.013"
                    }, 
                    "Biaya Kebutuhan Penjualan": {
                        "account_number": "5110.011"
                    }, 
                    "Biaya Kuli": {
                        "account_number": "5110.005"
                    }, 
                    "Biaya Leasing Kendaraan Operasional": {
                        "account_number": "5110.010"
                    }, 
                    "Biaya Parkir": {
                        "account_number": "5110.003"
                    }, 
                    "Biaya Penjualan Lain-lain": {
                        "account_number": "5110.018"
                    }, 
                    "Biaya Perbaikan Kendaraan Operasional": {
                        "account_number": "5110.008"
                    }, 
                    "Biaya Perjalanan Dinas": {
                        "account_number": "5110.006"
                    }, 
                    "Biaya Piutang Tak Tertagih": {
                        "account_number": "5110.016"
                    }, 
                    "Biaya Sewa Gudang": {
                        "account_number": "5110.014"
                    }, 
                    "Biaya Sewa Peralatan Gudang": {
                        "account_number": "5110.015"
                    }, 
                    "Biaya Susut Barang": {
                        "account_number": "5110.020"
                    }, 
                    "Biaya Tol": {
                        "account_number": "5110.002"
                    }, 
                    "Biaya Upah Angkat/Turun Barang": {
                        "account_number": "5110.004"
                    }, 
                    "Penyesuaian Persediaan": {
                        "account_number": "5110.019", 
                        "account_type": "Stock Adjustment"
                    }, 
                    "Potongan Supplier": {
                        "account_number": "5110.017"
                    }, 
                    "account_number": "5110.000"
                }, 
                "Biaya Gaji & Kesejahteraan Pegawai": {
                    "Biaya Asuransi Kesehatan Pegawai": {
                        "account_number": "5120.004"
                    }, 
                    "Biaya Gaji & Kesejahteraan Lainnya": {
                        "account_number": "5120.007"
                    }, 
                    "Biaya Gaji Karyawan Harian": {
                        "account_number": "5120.002"
                    }, 
                    "Biaya Gaji Staff & Karyawan Tetap": {
                        "account_number": "5120.001"
                    }, 
                    "Biaya Konsumsi": {
                        "account_number": "5120.006"
                    }, 
                    "Biaya Pengobatan": {
                        "account_number": "5120.003"
                    }, 
                    "Biaya THR, Bonus, dan Komisi": {
                        "account_number": "5120.005"
                    }, 
                    "account_number": "5120.000"
                }, 
                "Biaya Kantor & Gudang": {
                    "Biaya Alat Tulis Kantor": {
                        "account_number": "5130.005"
                    }, 
                    "Biaya Asuransi Bangunan": {
                        "account_number": "5130.014"
                    }, 
                    "Biaya Fotokopi, Foto, Cetak": {
                        "account_number": "5130.004"
                    }, 
                    "Biaya Humas & Pergaulan": {
                        "account_number": "5130.009"
                    }, 
                    "Biaya Kantor & Gudang Lain-lain": {
                        "account_number": "5130.018"
                    }, 
                    "Biaya PAM Gudang & Kantor": {
                        "account_number": "5130.002"
                    }, 
                    "Biaya PLN Gudang & Kantor": {
                        "account_number": "5130.001"
                    }, 
                    "Biaya Pemeliharaan Bangunan Gudang": {
                        "account_number": "5130.008"
                    }, 
                    "Biaya Perizinan Kendaraan Operasional": {
                        "account_number": "5130.017"
                    }, 
                    "Biaya Perizinan Usaha dan Bangunan": {
                        "account_number": "5130.016"
                    }, 
                    "Biaya Perlengkapan Gudang": {
                        "account_number": "5130.010"
                    }, 
                    "Biaya Serba Serbi": {
                        "account_number": "5130.012"
                    }, 
                    "Biaya Perbaikan Peralatan Gudang": {
                        "account_number": "5130.007"
                    }, 
                    "Biaya Sewa Kantor": {
                        "account_number": "5130.013"
                    }, 
                    "Biaya Materai & Pos": {
                        "account_number": "5130.006"
                    }, 
                    "Biaya Sumbangan": {
                        "account_number": "5130.015"
                    }, 
                    "Biaya Telpon Gudang & Kantor": {
                        "account_number": "5130.003"
                    }, 
                    "Biaya Iuran Bulanan": {
                        "account_number": "5130.011"
                    }, 
                    "account_number": "5130.000"
                }, 
                "account_number": "5100.000"
            }, 
            "Beban Tidak Langsung": {
                "Biaya Gaji & Kesejahteraan Pegawai Tidak Langsung": {
                    "Biaya Gaji Lain-lain": {
                        "account_number": "5210.005"
                    }, 
                    "Biaya Gaji Staff": {
                        "account_number": "5210.001"
                    }, 
                    "Biaya Konsumsi": {
                        "account_number": "5210.004"
                    }, 
                    "Biaya Pengobatan & Kesehatan": {
                        "account_number": "5210.003"
                    }, 
                    "Biaya THR dan Bonus Staff": {
                        "account_number": "5210.002"
                    }, 
                    "account_number": "5210.000"
                }, 
                "Biaya Kantor Tidak Langsung": {
                    "Biaya Alat Tulis Kantor": {
                        "account_number": "5230.006"
                    }, 
                    "Biaya Asuransi Bangunan": {
                        "account_number": "5230.005"
                    }, 
                    "Biaya Fotocopy, Photo, Print Out": {
                        "account_number": "5230.007"
                    }, 
                    "Biaya Iuran Bulanan": {
                        "account_number": "5230.012"
                    }, 
                    "Biaya Kantor Lain-lain": {
                        "account_number": "5230.016"
                    }, 
                    "Biaya Kirim Dokumen": {
                        "account_number": "5230.008"
                    }, 
                    "Biaya PAM Kantor": {
                        "account_number": "5230.002"
                    }, 
                    "Biaya PLN Kantor": {
                        "account_number": "5230.001"
                    }, 
                    "Biaya Pemeliharaan Bangunan Kantor": {
                        "account_number": "5230.011"
                    }, 
                    "Biaya Perizinan Bangunan": {
                        "account_number": "5230.014"
                    }, 
                    "Biaya Perizinan Kendaraan Dinas": {
                        "account_number": "5230.015"
                    }, 
                    "Biaya Perlengkapan & Peralatan Kantor": {
                        "account_number": "5230.009"
                    }, 
                    "Biaya Sewa Kantor": {
                        "account_number": "5230.004"
                    }, 
                    "Biaya Materai & Pos": {
                        "account_number": "5230.017"
                    }, 
                    "Biaya Sumbangan": {
                        "account_number": "5230.013"
                    }, 
                    "Biaya Telpon Kantor": {
                        "account_number": "5230.003"
                    }, 
                    "Biaya Perbaikan Peralatan Kantor": {
                        "account_number": "5230.010"
                    }, 
                    "account_number": "5230.000"
                }, 
                "Biaya Operasional Tidak Langsung": {
                    "Biaya Asuransi Kendaraan Dinas": {
                        "account_number": "5220.006"
                    }, 
                    "Biaya BBM": {
                        "account_number": "5220.001"
                    }, 
                    "Biaya Entertainment dan Pergaulan": {
                        "account_number": "5220.008"
                    }, 
                    "Biaya Hadiah dan Bonus": {
                        "account_number": "5220.009"
                    }, 
                    "Biaya Leasing Kendaraan Dinas": {
                        "account_number": "5220.007"
                    }, 
                    "Biaya Perbaikan Kendaraan Dinas": {
                        "account_number": "5220.005"
                    }, 
                    "Biaya Perjalanan Dinas": {
                        "account_number": "5220.004"
                    }, 
                    "Biaya Telpon & HP": {
                        "account_number": "5220.003"
                    }, 
                    "Biaya Tol & Parkir": {
                        "account_number": "5220.002"
                    }, 
                    "account_number": "5220.000"
                }, 
                "account_number": "5200.000"
            }, 
            "Biaya Penyusutan & Amortisasi": {
                "Biaya Penyusutan": {
                    "Biaya Penyusutan Aset": {
                        "account_number": "5310.001", 
                        "account_type": "Depreciation"
                    }, 
                    "account_number": "5310.000"
                }, 
                "Biaya Amortisasi": {
                    "Biaya Amortisasi": {
                        "account_number": "5320.001"
                    }, 
                    "account_number": "5320.000"
                }, 
                "account_number": "5300.000"
            }, 
            "account_number": "5000.000", 
            "root_type": "Expense"
        }, 
        "Ekuitas": {
            "Laba": {
                "Laba Usaha": {
                    "Laba Periode Berjalan": {
                        "account_number": "3213.001"
                    }, 
                    "Laba Tahun Berjalan": {
                        "account_number": "3212.001"
                    }, 
                    "Laba Ditahan": {
                        "account_number": "3211.001"
                    }, 
                    "account_number": "3210.000"
                },
                "account_number": "3200.000"
            },
            "Modal": {
                "Modal Usaha": {
                    "Modal di Setor": {
                        "account_number": "3111.001"
                    }, 
                    "Prive Pemegang Saham": {
                        "account_number": "3112.001"
                    }, 
                    "Saldo Pembukaan Modal": {
                        "account_number": "3113.001"
                    }, 
                    "account_number": "3110.000"
                },
                "account_number": "3100.000"
            },
            "account_number": "3000.000", 
            "root_type": "Equity"
        }, 
        "Passiva": {
            "Passiva Lancar": {
                "Biaya Yang Akan Dibayar": {
                    "Biaya Yang Akan Dibayar": {
                        "account_number": "2131.001"
                    }, 
                    "Biaya Yang Akan Dibayar - Biaya Kirim": {
                        "account_number": "2132.001", 
                        "account_type": "Expenses Included In Valuation"
                    }, 
                    "Gaji Yang Akan Dibayar": {
                        "account_number": "2133.001"
                    }, 
                    "Penggantian Biaya": {
                        "account_number": "2134.001"
                    }, 
                    "account_number": "2130.000"
                }, 
                "Hutang Dagang": {
                    "Hutang Dagang Biaya Kirim": {
                        "account_number": "2112.001", 
                        "account_type": "Payable"
                    }, 
                    "Hutang Dagang": {
                        "account_number": "2111.001", 
                        "account_type": "Payable"
                    }, 
                    "Barang Diterima Tapi Belum Ditagih": {
                        "account_number": "2115.001", 
                        "account_type": "Stock Received But Not Billed"
                    }, 
                    "account_number": "2110.000"
                }, 
                "Hutang Pajak": {
                    "Hutang Pajak": {
                        "account_number": "2140.001", 
                        "account_type": "Payable"
                    }, 
                    "account_number": "2140.000"
                }, 
                "Pendapatan Terima Dimuka": {
                    "Uang Muka Penjualan": {
                        "account_number": "2121.001", 
                        "account_type": "Bank"
                    }, 
                    "account_number": "2120.000"
                }, 
                "account_number": "2100.000"
            }, 
            "Passiva Tetap": {
                "Hutang Lain-lain": {
                    "Hutang Lain-lain": {
                        "account_number": "2290.001"
                    }, 
                    "account_number": "2290.000"
                }, 
                "Hutang Leasing Kendaraan": {
                    "Hutang Leasing Kendaraan": {
                        "account_number": "2230.001"
                    }, 
                    "account_number": "2230.000"
                }, 
                "Hutang Kepada Bank": {
                    "Pinjaman Pada Bank": {
                        "account_number": "2221.001"
                    }, 
                    "Hutang Bunga Pinjaman Pada Bank": {
                        "account_number": "2222.001"
                    }, 
                    "account_number": "2220.000"
                }, 
                "Hutang Kepada Pihak Ketiga": {
                    "Hutang Bunga Pinjaman Pada Pihak Ketiga": {
                        "account_number": "2213.001"
                    }, 
                    "Pinjaman Pada Pihak Ketiga Rutin": {
                        "account_number": "2211.001"
                    }, 
                    "Pinjaman Pada Pihak Ketiga Tidak Rutin": {
                        "account_number": "2212.001"
                    }, 
                    "account_number": "2210.000"
                }, 
                "account_number": "2200.000"
            }, 
            "account_number": "2000.000", 
            "root_type": "Liability"
        }, 
        "Pendapatan": {
            "Harga Pokok Pembelian": {
                "HPP Pembelian": {
                    "account_number": "4210.001", 
                    "account_type": "Cost of Goods Sold"
                }, 
                "account_number": "4200.000"
            }, 
            "Pendapatan Lain-lain": {
                "Pendapatan Bunga Bank": {
                    "account_number": "4410.001"
                }, 
                "Pendapatan Bunga Dari Pihak Ketiga": {
                    "account_number": "4420.001"
                }, 
                "Pendapatan Keuntungan Penjualan Aktiva": {
                    "account_number": "4430.001"
                }, 
                "Pendapatan Komisi": {
                    "account_number": "4440.001"
                }, 
                "Pendapatan Lain-lain": {
                    "account_number": "4480.001"
                }, 
                "Pendapatan Penjualan Barang Bekas": {
                    "account_number": "4460.001"
                }, 
                "Pendapatan Sewa Gudang": {
                    "account_number": "4450.001"
                }, 
                "Pendapatan Sewa Lain-lain": {
                    "account_number": "4490.001"
                }, 
                "account_number": "4400.000"
            }, 
            "Pendapatan Jasa": {
                "Pendapatan Jasa": {
                    "account_number": "4310.001"
                }, 
                "account_number": "4300.000"
            }, 
            "Penjualan Barang": {
                "Penjualan Barang Dagang": {
                    "account_number": "4110.001"
                }, 
                "Potongan Penjualan": {
                    "account_number": "4130.001"
                }, 
                "Retur Penjualan": {
                    "account_number": "4120.001"
                }, 
                "account_number": "4100.000"
            }, 
            "account_number": "4000.000", 
            "root_type": "Income"
        }
    }
