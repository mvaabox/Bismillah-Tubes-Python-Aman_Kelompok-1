import csv

while True: # Untuk melakukan perulangan

    def bacaCSV(dir_File):
        kel1 = open(dir_File)
        next(kel1) # skip 1 kolom (header)
        testData = []
        ygBaru = []
        x = []
        for nama in kel1:
            kolom = nama.delimiter(';')

            # Cek nilai/data yang tertukar
            if len(kolom)[0] < 7:
                if len(kolom[1]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[1]
                    kolom[1] = temp
                elif len(kolom[2]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[2]
                    kolom[2] = temp
                elif len(kolom[3]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[3]
                    kolom[3] = temp
                elif len(kolom[4]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[4]
                    kolom[4] = temp
                elif len(kolom[5]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[5]
                    kolom[5] = temp
                elif len(kolom[6]) >= 7:
                    temp = kolom[0]
                    kolom[0] = kolom[6]
                    kolom[6] = temp
                elif len(kolom[0]) > 6:
                    pass
                else :
                    continue
        kel1.close()
        return ygBaru
        
    # Ubah tipe data menjadi integer    
    def changeType(testData):
        for b in range(len(testData)):
            for c in range(1, len(testData[b])):
                if testData[b][c] != str:
                    testData[b][c] = float(testData[b][c])
                    testData[b][c] = int(testData[b][c])
        return testData


        # Hitung rata-rata (Mean)
        def rata(data_kolom):
            sum = 0
            rataVal = 0
            for b in range(1, len(testData)):
                sum += testData[b][data_kolom]
            rataVal = sum // len(testData)
            return rataVal


        # Cari nilai tengah (Median)
        def median(tengah):
            listBaru = []
            for b in range(1, len(testData)):
                listBaru.append(testData[b][tengah])
            if len(listBaru) % 2 == 0:
                q1 = listBaru[len(listBaru) // 2]
                q2 = listBaru[len(listBaru) // 2 - 1]
                median = (q1 + q2) / 2
            else:
                median = listBaru[len(listBaru) // 2]
            return median