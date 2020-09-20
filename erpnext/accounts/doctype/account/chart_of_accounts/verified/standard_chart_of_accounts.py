# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
from frappe import _

def get():
	return {
        "Aktiva": {
            "Aktiva Lancar": {
                "Akun sementara": {
                    "Pembukaan sementara": {"account_type": "Temporary"}, 
                }, 
                "Bank ": {
                    "Rekening Bank": {"account_type": "Bank", "is_group": 1}, 
                }, 
                "Biaya Bayar Dimuka": {
                    "Biaya Bayar Dimuka": {}, 
                }, 
                "Kas": {
                    "Kas Besar": {"account_type": "Cash"}, 
                    "Kas Kecil": {"account_type": "Cash"}, 
                }, 
                "Pendapatan Yang Akan Diterima": {
                    "Pendapatan Yang Akan Diterima": {}, 
                }, 
                "Persediaan Barang": {
                    "Persediaan Barang": {"account_type": "Stock"}, 
                    "Uang Muka Pembelian": {"account_type": "Bank"}, 
                }, 
                "Piutang": {
                    "Piutang Dagang": {"account_type": "Receivable"}, 
                    "Piutang Karyawan": {"account_type": "Receivable"}, 
                    "Piutang Lain-lain": {"account_type": "Receivable"}, 
                }, 
            }, 
            "Aktiva Tetap": {
                "Aset": {
                    "Bangunan": {"account_type": "Fixed Asset"}, 
                    "Kendaraan": {"account_type": "Fixed Asset"}, 
                    "Mesin & Peralatan": {"account_type": "Fixed Asset"},
                },
                "Akumulasi Penyusutan Aset": {
                    "Akumulasi Penyusutan Aset": {"account_type": "Accumulated Depreciation"}, 
                }, 
                "Investasi": {
                    "Deposito": {}, 
                    "Investasi Surat Berharga": {}, 
                    "Investasi Properti": {}, 
                }, 
                "Aktiva Tetap Lainnya": {
                    "Biaya Ditangguhkan": {}, 
                }, 
            }, 
            "root_type": "Asset"
        }, 
        "Pengeluaran": {
            "Beban Lain-lain": {
                "Beban Lain-lain": {
                    "Beban Administrasi Bank": {}, 
                    "Beban Bunga Kredit Rekening Koran Bank": {}, 
                    "Beban Bunga Pinjaman Pada Pihak Ketiga": {}, 
                    "Beban Notaris Dan Administrasi Kredit Bank": {}, 
                    "Beban Pajak Bumi & Bangunan": {"account_type": "Tax"}, 
                    "Beban Pajak PPN": {"account_type": "Tax"}, 
                    "Beban Pajak Penghasilan ": {"account_type": "Tax"}, 
                    "Beban Provisi Pinjaman Bank": {}, 
                    "Selisih Kurs": {"account_type": "Round Off"}, 
                    "Selisih Pembayaran Pembeli": {"account_type": "Round Off"}, 
                }, 
            }, 
            "Beban Langsung": {
                "Beban Penjualan": {
                    "Biaya Asuransi Kendaraan Operasional": {}, 
                    "Biaya BBM": {}, 
                    "Biaya Barang Rusak": {}, 
                    "Biaya Bonus, Hadiah, dan Sampel": {}, 
                    "Biaya Entertainment dan Pergaulan": {}, 
                    "Biaya Kebutuhan Penjualan": {}, 
                    "Biaya Kuli": {}, 
                    "Biaya Leasing Kendaraan Operasional": {}, 
                    "Biaya Parkir": {}, 
                    "Biaya Penjualan Lain-lain": {}, 
                    "Biaya Perbaikan Kendaraan Operasional": {}, 
                    "Biaya Perjalanan Dinas": {}, 
                    "Biaya Piutang Tak Tertagih": {}, 
                    "Biaya Sewa Gudang": {}, 
                    "Biaya Sewa Peralatan Gudang": {}, 
                    "Biaya Susut Barang": {}, 
                    "Biaya Tol": {}, 
                    "Biaya Upah Angkat/Turun Barang": {}, 
                    "Penyesuaian Persediaan": {"account_type": "Stock Adjustment"}, 
                    "Potongan Supplier": {}, 
                }, 
                "Biaya Gaji & Kesejahteraan Pegawai": {
                    "Biaya Asuransi Kesehatan Pegawai": {}, 
                    "Biaya Gaji & Kesejahteraan Lainnya": {}, 
                    "Biaya Gaji Karyawan Harian": {}, 
                    "Biaya Gaji Staff & Karyawan Tetap": {}, 
                    "Biaya Konsumsi": {}, 
                    "Biaya Pengobatan": {}, 
                    "Biaya THR, Bonus, dan Komisi": {}, 
                }, 
                "Biaya Kantor & Gudang": {
                    "Biaya Alat Tulis Kantor": {}, 
                    "Biaya Asuransi Bangunan": {}, 
                    "Biaya Fotokopi, Foto, Cetak": {}, 
                    "Biaya Humas & Pergaulan": {}, 
                    "Biaya Kantor & Gudang Lain-lain": {}, 
                    "Biaya PAM Gudang & Kantor": {}, 
                    "Biaya PLN Gudang & Kantor": {}, 
                    "Biaya Pemeliharaan Bangunan Gudang": {}, 
                    "Biaya Perizinan Kendaraan Operasional": {}, 
                    "Biaya Perizinan Usaha dan Bangunan": {}, 
                    "Biaya Perlengkapan Gudang": {}, 
                    "Biaya Serba Serbi": {}, 
                    "Biaya Perbaikan Peralatan Gudang": {}, 
                    "Biaya Sewa Kantor": {}, 
                    "Biaya Materai & Pos": {}, 
                    "Biaya Sumbangan": {}, 
                    "Biaya Telpon Gudang & Kantor": {}, 
                    "Biaya Iuran Bulanan": {}, 
                }, 
            }, 
            "Beban Tidak Langsung": {
                "Biaya Gaji & Kesejahteraan Pegawai Tidak Langsung": {
                    "Biaya Gaji Lain-lain": {}, 
                    "Biaya Gaji Staff": {}, 
                    "Biaya Konsumsi": {}, 
                    "Biaya Pengobatan & Kesehatan": {}, 
                    "Biaya THR dan Bonus Staff": {}, 
                }, 
                "Biaya Kantor Tidak Langsung": {
                    "Biaya Alat Tulis Kantor": {}, 
                    "Biaya Asuransi Bangunan": {}, 
                    "Biaya Fotocopy, Photo, Print Out": {}, 
                    "Biaya Iuran Bulanan": {}, 
                    "Biaya Kantor Lain-lain": {}, 
                    "Biaya Kirim Dokumen": {}, 
                    "Biaya PAM Kantor": {}, 
                    "Biaya PLN Kantor": {}, 
                    "Biaya Pemeliharaan Bangunan Kantor": {}, 
                    "Biaya Perizinan Bangunan": {}, 
                    "Biaya Perizinan Kendaraan Dinas": {}, 
                    "Biaya Perlengkapan & Peralatan Kantor": {}, 
                    "Biaya Sewa Kantor": {}, 
                    "Biaya Materai & Pos": {}, 
                    "Biaya Sumbangan": {}, 
                    "Biaya Telpon Kantor": {}, 
                    "Biaya Perbaikan Peralatan Kantor": {}, 
                }, 
                "Biaya Operasional Tidak Langsung": {
                    "Biaya Asuransi Kendaraan Dinas": {}, 
                    "Biaya BBM": {}, 
                    "Biaya Entertainment dan Pergaulan": {}, 
                    "Biaya Hadiah dan Bonus": {}, 
                    "Biaya Leasing Kendaraan Dinas": {}, 
                    "Biaya Perbaikan Kendaraan Dinas": {}, 
                    "Biaya Perjalanan Dinas": {}, 
                    "Biaya Telpon & HP": {}, 
                    "Biaya Tol & Parkir": {}, 
                }, 
            }, 
            "Biaya Penyusutan & Amortisasi": {
                "Biaya Penyusutan": {
                    "Biaya Penyusutan Aset": {"account_type": "Depreciation"}, 
                }, 
                "Biaya Amortisasi": {
                    "Biaya Amortisasi": {}, 
                }, 
            }, 
            "root_type": "Expense"
        }, 
        "Ekuitas": {
            "Laba": {
                "Laba Usaha": {
                    "Laba Periode Berjalan": {}, 
                    "Laba Tahun Berjalan": {}, 
                    "Laba Ditahan": {}, 
                },
            },
            "Modal": {
                "Modal Usaha": {
                    "Modal di Setor": {}, 
                    "Prive Pemegang Saham": {}, 
                    "Saldo Pembukaan Modal": {}, 
                },
            },
            "root_type": "Equity"
        }, 
        "Passiva": {
            "Passiva Lancar": {
                "Biaya Yang Akan Dibayar": {
                    "Biaya Yang Akan Dibayar": {}, 
                    "Biaya Yang Akan Dibayar - Biaya Kirim": {"account_type": "Expenses Included In Valuation"}, 
                    "Gaji Yang Akan Dibayar": {}, 
                    "Penggantian Biaya": {}, 
                }, 
                "Hutang Dagang": {
                    "Hutang Dagang Biaya Kirim": {"account_type": "Payable"}, 
                    "Hutang Dagang": {"account_type": "Payable"}, 
                    "Barang Diterima Tapi Belum Ditagih": {"account_type": "Stock Received But Not Billed"}, 
                }, 
                "Hutang Pajak": {
                    "Hutang Pajak": {"account_type": "Payable"}, 
                }, 
                "Pendapatan Terima Dimuka": {
                    "Uang Muka Penjualan": {"account_type": "Bank"}, 
                }, 
            }, 
            "Passiva Tetap": {
                "Hutang Lain-lain": {
                    "Hutang Lain-lain": {}, 
                }, 
                "Hutang Leasing Kendaraan": {
                    "Hutang Leasing Kendaraan": {}, 
                }, 
                "Hutang Kepada Bank": {
                    "Pinjaman Pada Bank": {}, 
                    "Hutang Bunga Pinjaman Pada Bank": {}, 
                }, 
                "Hutang Kepada Pihak Ketiga": {
                    "Hutang Bunga Pinjaman Pada Pihak Ketiga": {}, 
                    "Pinjaman Pada Pihak Ketiga Rutin": {}, 
                    "Pinjaman Pada Pihak Ketiga Tidak Rutin": {}, 
                }, 
            }, 
            "root_type": "Liability"
        }, 
        "Pendapatan": {
            "Harga Pokok Pembelian": {
                "HPP Pembelian": {"account_type": "Cost of Goods Sold"}, 
            }, 
            "Pendapatan Lain-lain": {
                "Pendapatan Bunga Bank": {}, 
                "Pendapatan Bunga Dari Pihak Ketiga": {}, 
                "Pendapatan Keuntungan Penjualan Aktiva": {}, 
                "Pendapatan Komisi": {}, 
                "Pendapatan Lain-lain": {}, 
                "Pendapatan Penjualan Barang Bekas": {}, 
                "Pendapatan Sewa Gudang": {}, 
                "Pendapatan Sewa Lain-lain": {}, 
            }, 
            "Pendapatan Jasa": {
                "Pendapatan Jasa": {}, 
            }, 
            "Penjualan Barang": {
                "Penjualan Barang Dagang": {}, 
                "Potongan Penjualan": {}, 
                "Retur Penjualan": {}, 
            }, 
            "root_type": "Income"
        }
    }
