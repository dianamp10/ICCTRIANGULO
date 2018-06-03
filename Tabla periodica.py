# Variables:
ma = "Metales Alcalinos"
mt = "Metales de Transicion"
mat = "Metales Alcalinoterreos"
ml = "Metaloide"
sm = "Semiconductores"
ac = "Actinidos"
nm = "No Metal"
ha = "Halogenos"
la = "Lantanidos"
gn = "Gases Nobles"

# Listas:
simbolo = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og", "Uu", "Ub"]
nombre = ["Hidrogeno", "Helio", "Litio", "Berilio", "Boro", "Carbono", "Nitrogeno", "Oxigeno", "Fluor", "Neon", "Sodio", "Magnesio", "Aluminio", "Silicio", "Fosforo", "Azufre", "Cloro", "Argon", "Potasio", "Calcio", "Escandio", "Titanio", "Vanadio", "Cromo", "Manganeso", "Hierro", "Cobalto", "Niquel", "Cobre", "Cinc", "Galio", "Germanio", "Arsenico", "Selenio", "Bromo", "Kripton", "Rubidio", "Estroncio", "Itrio", "Circonio", "Niobio", "Molibdeno", "Tecnecio", "Rutenio", "Rodio", "Paladio", "Plata", "Cadmio", "Indio", "Estaño", "Antimonio", "Telurio", "Yodo", "Xenon", "Cesio", "Bario", "Lantano", "Cerio", "Praseodimio", "Neodimio", "Prometio", "Samario", "Europio", "Gadolinio", "Terbio", "Disprosio", "Holmio", "Erbio", "Tulio", "Iterbio", "Lutecio", "Hafnio", "Tantalo", "Tungsteno", "Renio", "Osnio", "Iridio", "Platino", "Oro", "Mercurio", "Talio", "Plomo", "Bismuto", "Polonio", "Astato", "Radon", "Francio", "Radio", "Actinio", "Torio", "Protactinio", "Uranio", "Neptunio", "Plutonio", "Americio", "Curio", "Berkelio", "Californio", "Einstenio", "Fermio", "Mendelevio", "Nobelio", "Lawrencio", "Rutherfordio", "Dubnio", "Seaborgio", "Bohrio", "Hasio", "Meitnerio", "Darmstatio", "Roentgenio", "Copernicio", "Nihonio", "Flerovio", "Moscovio", "Livermorio", "Teneso", "Oganeson", "Ununennio", "Unbinilio"]
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120]
categoria = [nm, gn, ma, mat, ml, nm, nm, nm, ha, gn, ma, mat, sm, ml, nm, nm, ha, gn, ma, mat, mt, mt, mt, mt, mt, mt, mt, mt, mt, mt, sm, ml, ml, nm, ha, gn, ma, mat, mt, mt, mt, mt, mt, mt, mt, mt, mt, mt, sm, sm, ml, ml, ha, ma, ma, mat, la, la, la, la, la, la, la, la, la, la, la, la, la, la, la, mt, mt, mt, mt, mt, mt, mt, mt, mt, sm, sm, sm, ml, ha, gn, ma, ma, ac, ac, ac, ac, ac, ac, ac, ac, ac, ac, ac, ac, ac, ac, ac, mt, mt, mt, mt, mt, mt, mt, mt, mt, sm, sm, sm, sm, ha, gn, ma, mat]
peso = [1, 4, 7, 9, 10.8, 12, 14, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 40, 39, 40, 45, 48, 51, 52, 55, 55.8, 59, 58.6, 63.5, 65.4, 69.7, 72.6, 65, 79, 80, 83.7, 85, 87.6, 89, 91, 93, 96, 99, 101, 103, 106, 107.8, 112.4, 114.8, 118.7, 121.7, 127.6, 127, 131, 133, 137, 139, 140, 141, 144, 147, 150, 152, 157, 159, 162.5, 165, 167, 169, 173, 175, 178.4, 181, 183.8, 186, 190, 192, 195, 197, 200, 204, 207, 209, 209, 210, 222, 223, 226, 227, 232, 231, 238, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 266, 267, 268, 272, 274, 276, 278, 281, 283, 285, 287, 289, 291, 293, 294, 294, 316, 320]
radiactivo = ["No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "Es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "No es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "Es radiactivo", "No es radiactivo", "No es radiactivo"]



n=input("ingrese el elemento:")
metales_alcalinos=["litio","sodio","potasio","rubidio","cesio","francio"]
metales_de_transicion=["escandio" ,"Titanio" "Vanadio","Cromo","Manganeso","Hierro","Cobalto","Níquel","Cobre","Zinc","Itrio","Zirconio","Niobio","Molibdeno","Tecnecio","Rutenio","Rodio","Paladio","Plata","Cadmio","Lutecio","Hafnio","Tantalio","Wolframio","Renio","Osmio","Iridio","Platino","Oro","Mercurio","Laurencio","Rutherfordio","Dubnio","Seaborgio","Bohrio","Hassio","Meitnerio","Darmstadtio","Roentgenio","Copernicio"]
metales_alcanoterreos=["berilio", "magnesio","calcio","estroncio","bario","radio"]
metaloides=["boro","Silicio","Germanio","Arsénico","Antimonio","Telurio","Polonio","Ástato"]
actinidos=["Actinio","Torio","Protactinio","Uranio","Neptunio","Plutonio","Americio","Curio","Berkelio","Californio","Einstenio","Fermio","Mendelevio","Nobelio""Laurencio"]
no_metales=["Hidrógeno","Carbono","Nitrógeno","Oxígeno","Flúor","Fósforo","Azufre","Cloro","Selenio","Bromo","Yodo","Astato"]
halogenos=["flúor","cloro","bromo","yodo","astato","téneso"]
if n in list(metales_alcalinos):
    print("metal alcalino")
elif n in list(metales_de_transicion):
    print("metal de transicion")
elif n in list(metales_alcanoterreos):
    print("metal alcanoterreo")
elif n in list(metaloides):
    print("metaloide")
elif n in list(actinidos):
    print("actinido")
elif n in list(no_metales):
    print("no metal")
elif n in list(halogenos):
    print("halogeno")

def bubbleSort(alist,blist,clist,dlist,elist):
    for passnum in range(len(alist)(0,119,1)):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp1 = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp1

                temp2 = blist[i]
                blist[i] = blist[i+1]
                blist[i+1] = temp2

                temp3 = clist[i]
                clist[i] = clist[i+1]
                clist[i+1] = temp3

                temp4 = dlist[i]
                dlist[i] = dlist[i+1]
                dlist[i+1] = temp4

                temp5 = elist[i]
                elist[i] = elist[i+1]
                elist[i+1] = temp5

                temp6 = flist[i]
                flist[i] = flist[i+1]
                flist[i+1] = temp6

bubbleSort(simbolo,nombre,numero,categoria,peso,radiactivo)

val = int(input())
if val in numero:
    print(simbolo[val], nombre[val], numero[val], categoria[val], peso[val], radiactivo[val])

