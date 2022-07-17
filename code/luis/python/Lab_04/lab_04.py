numbers_in_english_ones = {
    '0':'Zero',
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five',
    '6':'Six',
    '7':'Seven',
    '8':'Eight',
    '9':'Nine',
}
numbers_in_english_tens ={
    '10': "Ten",
    '11': 'Eleven',
    '12': 'Twelve',
    '13': 'Thirteen',
    '14': 'Fourteen',
    '15': 'fifteen',
    '16': 'Sixteen',
    '17': 'Seventeen',
    '18': 'Eighteen',
    '19': 'nineteen',
    '20': "Twenty",
    '30': "Thirty",
    '40': "Forty",
    '50': "Fifty",
    '60': "Sixty",
    '70': "Seventy",
    '80': "Eighty",
    '90': "Ninety"
}
number_in_english_hundreds = {
    "1": "One Hundred",
    "2": "Two Hundred",
    "3": "Three Hundred",
    "4": " Four Hundred",
    "5": "Five Hundred",
    "6": "Six Hundred",
    "7": "Seven Hundred",
    "8": "Eight Hundred",
    "9": "Nine Hundred"
}



x = int(input("Enter a two digit number, from 0-99: "))
ones = x%10
tens = x//10
hundred = x*1
# prints three digits to english
if x == 100:
    print(number_in_english_hundreds["1"])
elif x == 101:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["1"])
elif x == 102:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["2"])
elif x == 103:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["3"])
elif x == 104:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["4"])
elif x == 105:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["5"])
elif x == 106:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["6"])
elif x == 107:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["7"])
elif x == 108:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["8"])
elif x == 109:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["9"])
elif x == 110:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["10"])
elif x == 111:
    print(number_in_english_hundreds["1"], 'and',numbers_in_english_tens["11"])
elif x == 112:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["12"])
elif x == 113:
    print(number_in_english_hundreds["1"],'and', numbers_in_english_tens["13"])
elif x == 114:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["14"])
elif x == 115:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["15"])
elif x == 116:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["16"])
elif x == 117:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["17"])
elif x == 118:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["18"])
elif x == 119:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["19"])
elif x == 120:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"])
elif x == 121:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["1"])
elif x == 122:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["2"])
elif x == 123:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["3"])
elif x == 124:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["4"])
elif x == 125:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["5"])
elif x == 126:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["6"])
elif x == 127:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["7"])
elif x == 128:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["8"])
elif x == 129:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["9"])
elif x == 130:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"])
elif x == 131:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["1"])
elif x == 132:
    print(number_in_english_hundreds["1"],'and', numbers_in_english_tens["30"],numbers_in_english_ones["2"])
elif x == 133:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["3"])
elif x == 134:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["4"])
elif x == 135:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["5"]) 
elif x == 136:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["6"])
elif x == 137:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["7"])
elif x == 138:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["8"])
elif x == 139:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["9"])
elif x == 140:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"])
elif x == 141:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["1"])
elif x == 142:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["2"])
elif x == 143:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["3"])
elif x == 144:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["4"])
elif x == 145:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["5"])
elif x == 146:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["6"])
elif x == 147:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["7"])
elif x == 148:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["8"])
elif x == 149:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["9"])
elif x == 150:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"])
elif x == 151:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["1"])
elif x == 152:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["2"])
elif x == 153:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["3"])
elif x == 154:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["4"])
elif x == 155:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["5"])
elif x == 156:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["6"])
elif x == 157:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["7"])
elif x == 158:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["8"])
elif x == 159:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["9"])
elif x == 160:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"])
elif x == 161:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["1"])
elif x == 162:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["2"])
elif x == 163:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["3"])
elif x == 164:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["4"])
elif x == 165:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["5"])
elif x == 166:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["6"])
elif x == 167:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["7"])
elif x == 168:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["8"])
elif x == 169:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["9"])
elif x == 170:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"])
elif x == 171:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["1"])
elif x == 172:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["2"])
elif x == 173:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["3"])
elif x == 174:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["4"])
elif x == 175:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["5"])
elif x == 176:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["6"])
elif x == 177:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["7"])
elif x == 178:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["8"])
elif x == 179:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["9"])
elif x == 180:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"])
elif x == 181:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["1"])
elif x == 182:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["2"])
elif x == 183:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["3"])
elif x == 184:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["4"])
elif x == 185:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["5"])
elif x == 186:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["6"])
elif x == 187:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["7"])
elif x == 188:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["8"])
elif x == 189:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["9"])
elif x == 190:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"])
elif x == 191:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["1"])
elif x == 192:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["2"])
elif x == 193:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["3"])
elif x == 194:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["4"])
elif x == 195:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["5"])
elif x == 196:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["6"])
elif x == 197:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["7"])
elif x == 198:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["8"])
elif x == 199:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["9"])
#############################################################################################################
elif x == 200:
    print(number_in_english_hundreds["2"])
elif x == 201:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["1"])
elif x == 202:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["2"])
elif x == 203:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["3"])
elif x == 204:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["4"])
elif x == 205:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["5"])
elif x == 206:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["6"])
elif x == 207:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["7"])
elif x == 208:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["8"])
elif x == 209:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_ones["9"])
elif x == 210:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["10"])
elif x == 211:
    print(number_in_english_hundreds["2"], 'and',numbers_in_english_tens["11"])
elif x == 212:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["12"])
elif x == 213:
    print(number_in_english_hundreds["2"],'and', numbers_in_english_tens["13"])
elif x == 214:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["14"])
elif x == 215:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["15"])
elif x == 216:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["16"])
elif x == 217:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["17"])
elif x == 218:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["18"])
elif x == 219:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["19"])
elif x == 220:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"])
elif x == 221:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["1"])
elif x == 222:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["2"])
elif x == 223:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["3"])
elif x == 224:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["4"])
elif x == 225:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["5"])
elif x == 226:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["6"])
elif x == 227:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["7"])
elif x == 228:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["8"])
elif x == 229:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["9"])
elif x == 230:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"])
elif x == 231:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["1"])
elif x == 232:
    print(number_in_english_hundreds["2"],'and', numbers_in_english_tens["30"],numbers_in_english_ones["2"])
elif x == 233:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["3"])
elif x == 234:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["4"])
elif x == 235:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["5"]) 
elif x == 236:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["6"])
elif x == 237:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["7"])
elif x == 238:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["8"])
elif x == 239:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["9"])
elif x == 240:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"])
elif x == 241:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["1"])
elif x == 242:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["2"])
elif x == 243:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["3"])
elif x == 244:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["4"])
elif x == 245:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["5"])
elif x == 246:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["6"])
elif x == 247:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["7"])
elif x == 248:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["8"])
elif x == 249:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["9"])
elif x == 250:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"])
elif x == 251:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["1"])
elif x == 252:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["2"])
elif x == 253:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["3"])
elif x == 254:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["4"])
elif x == 255:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["5"])
elif x == 256:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["6"])
elif x == 257:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["7"])
elif x == 258:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["8"])
elif x == 259:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["9"])
elif x == 260:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"])
elif x == 261:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["1"])
elif x == 262:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["2"])
elif x == 263:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["3"])
elif x == 264:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["4"])
elif x == 265:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["5"])
elif x == 266:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["6"])
elif x == 267:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["7"])
elif x == 268:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["8"])
elif x == 269:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["9"])
elif x == 270:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"])
elif x == 271:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["1"])
elif x == 272:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["2"])
elif x == 273:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["3"])
elif x == 274:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["4"])
elif x == 275:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["5"])
elif x == 276:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["6"])
elif x == 277:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["7"])
elif x == 278:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["8"])
elif x == 279:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["9"])
elif x == 280:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"])
elif x == 281:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["1"])
elif x == 282:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["2"])
elif x == 283:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["3"])
elif x == 284:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["4"])
elif x == 285:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["5"])
elif x == 286:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["6"])
elif x == 287:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["7"])
elif x == 288:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["8"])
elif x == 289:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["9"])
elif x == 290:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"])
elif x == 291:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["1"])
elif x == 292:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["2"])
elif x == 293:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["3"])
elif x == 294:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["4"])
elif x == 295:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["5"])
elif x == 296:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["6"])
elif x == 297:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["7"])
elif x == 298:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["8"])
elif x == 299:
    print(number_in_english_hundreds["2"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["9"])
###########################################################################################################
elif x == 300:


###############################################################################
    print(number_in_english_hundreds["3"])
elif x == 101:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["1"])
elif x == 102:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["2"])
elif x == 103:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["3"])
elif x == 104:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["4"])
elif x == 105:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["5"])
elif x == 106:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["6"])
elif x == 107:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["7"])
elif x == 108:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["8"])
elif x == 109:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_ones["9"])
elif x == 110:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["10"])
elif x == 111:
    print(number_in_english_hundreds["1"], 'and',numbers_in_english_tens["11"])
elif x == 112:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["12"])
elif x == 113:
    print(number_in_english_hundreds["1"],'and', numbers_in_english_tens["13"])
elif x == 114:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["14"])
elif x == 115:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["15"])
elif x == 116:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["16"])
elif x == 117:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["17"])
elif x == 118:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["18"])
elif x == 119:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["19"])
elif x == 120:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"])
elif x == 121:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["1"])
elif x == 122:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["2"])
elif x == 123:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["3"])
elif x == 124:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["4"])
elif x == 125:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["5"])
elif x == 126:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["6"])
elif x == 127:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["7"])
elif x == 128:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["8"])
elif x == 129:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["20"],numbers_in_english_ones["9"])
elif x == 130:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"])
elif x == 131:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["1"])
elif x == 132:
    print(number_in_english_hundreds["1"],'and', numbers_in_english_tens["30"],numbers_in_english_ones["2"])
elif x == 133:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["3"])
elif x == 134:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["4"])
elif x == 135:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["5"]) 
elif x == 136:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["6"])
elif x == 137:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["7"])
elif x == 138:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["8"])
elif x == 139:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["30"],numbers_in_english_ones["9"])
elif x == 140:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"])
elif x == 141:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["1"])
elif x == 142:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["2"])
elif x == 143:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["3"])
elif x == 144:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["4"])
elif x == 145:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["5"])
elif x == 146:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["6"])
elif x == 147:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["7"])
elif x == 148:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["8"])
elif x == 149:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["40"],numbers_in_english_ones["9"])
elif x == 150:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"])
elif x == 151:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["1"])
elif x == 152:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["2"])
elif x == 153:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["3"])
elif x == 154:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["4"])
elif x == 155:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["5"])
elif x == 156:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["6"])
elif x == 157:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["7"])
elif x == 158:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["8"])
elif x == 159:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["50"],numbers_in_english_ones["9"])
elif x == 160:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"])
elif x == 161:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["1"])
elif x == 162:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["2"])
elif x == 163:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["3"])
elif x == 164:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["4"])
elif x == 165:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["5"])
elif x == 166:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["6"])
elif x == 167:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["7"])
elif x == 168:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["8"])
elif x == 169:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["60"],numbers_in_english_ones["9"])
elif x == 170:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"])
elif x == 171:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["1"])
elif x == 172:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["2"])
elif x == 173:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["3"])
elif x == 174:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["4"])
elif x == 175:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["5"])
elif x == 176:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["6"])
elif x == 177:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["7"])
elif x == 178:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["8"])
elif x == 179:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["70"],numbers_in_english_ones["9"])
elif x == 180:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"])
elif x == 181:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["1"])
elif x == 182:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["2"])
elif x == 183:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["3"])
elif x == 184:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["4"])
elif x == 185:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["5"])
elif x == 186:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["6"])
elif x == 187:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["7"])
elif x == 188:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["8"])
elif x == 189:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["80"],numbers_in_english_ones["9"])
elif x == 190:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"])
elif x == 191:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["1"])
elif x == 192:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["2"])
elif x == 193:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["3"])
elif x == 194:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["4"])
elif x == 195:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["5"])
elif x == 196:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["6"])
elif x == 197:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["7"])
elif x == 198:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["8"])
elif x == 199:
    print(number_in_english_hundreds["1"],'and',numbers_in_english_tens["90"],numbers_in_english_ones["9"])
##############################################################################################################
elif x == 400:
    print(number_in_english_hundreds["4"])
elif x == 500:
    print(number_in_english_hundreds["5"])
elif x == 600:
    print(number_in_english_hundreds["6"])
elif x == 700:
    print(number_in_english_hundreds["7"])
elif x == 800:
    print(number_in_english_hundreds["8"])
elif x == 900:
    print(number_in_english_hundreds["9"])


# prints two digits to english
if tens_digit == 0 and ones_digit == 0:
    print("Zero")
elif tens_digit == 0 and ones_digit == 1:
    print("One")
elif tens_digit == 0 and ones_digit == 2:
    print("Two")
elif tens_digit == 0 and ones_digit == 3:
    print("Three")
elif tens_digit == 0 and ones_digit == 4:
    print("four")
elif tens_digit == 0 and ones_digit == 5:
    print("Five")
elif tens_digit == 0 and ones_digit == 6:
    print("Six")
elif tens_digit == 0 and ones_digit == 7:
    print("Seven")
elif tens_digit == 0 and ones_digit == 8:
    print("Eight")
elif tens_digit == 0 and ones_digit == 9:
    print("Nine")
elif tens_digit == 1 and ones_digit == 0:
    print("ten")
elif tens_digit == 1 and ones_digit == 1:
    print(numbers_in_english_tens["11"])
elif tens_digit == 1 and ones_digit == 2:
    print(numbers_in_english_tens["12"])
elif tens_digit == 1 and ones_digit == 3:
    print(numbers_in_english_tens["13"])
elif tens_digit == 1 and ones_digit == 4:
    print(numbers_in_english_tens["14"])
elif tens_digit == 1 and ones_digit == 5:
    print(numbers_in_english_tens["15"])
elif tens_digit == 1 and ones_digit == 6:
    print(numbers_in_english_tens["16"])
elif tens_digit == 1 and ones_digit == 7:
    print(numbers_in_english_tens["17"])
elif tens_digit == 1 and ones_digit == 8:
    print(numbers_in_english_tens["18"])
elif tens_digit == 1 and ones_digit == 9:
    print(numbers_in_english_tens["19"])
elif tens_digit == 2 and ones_digit == 0:
    print(numbers_in_english_tens["20"])
elif tens_digit == 2 and ones_digit == 1:
    print(numbers_in_english_tens["20"],"-",numbers_in_english_ones['1'])
elif tens_digit == 2 and ones_digit == 2:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["2"])
elif tens_digit == 2 and ones_digit == 3:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["3"])
elif tens_digit == 2 and ones_digit == 4:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["4"])
elif tens_digit == 2 and ones_digit == 5:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["5"])
elif tens_digit == 2 and ones_digit == 6:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["6"])
elif tens_digit == 2 and ones_digit == 7:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["7"])
elif tens_digit == 2 and ones_digit == 8:
    print(numbers_in_english_tens["20"],'-',numbers_in_english_ones["8"])
elif tens_digit == 2 and ones_digit == 9:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["9"])
elif tens_digit == 3 and ones_digit == 10:
    print(numbers_in_english_tens["30"])
elif tens_digit == 3 and ones_digit == 1:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["1"])
elif tens_digit == 3 and ones_digit == 2:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["2"])
elif tens_digit == 3 and ones_digit == 3:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["3"])
elif tens_digit == 3 and ones_digit == 4:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["4"])
elif tens_digit == 3 and ones_digit == 5:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["5"])
elif tens_digit == 3 and ones_digit == 6:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["6"])
elif tens_digit == 3 and ones_digit == 7:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["7"])
elif tens_digit == 3 and ones_digit == 8:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["8"])
elif tens_digit == 3 and ones_digit == 9:
    print(numbers_in_english_tens["30"],'-',numbers_in_english_ones["9"])
elif tens_digit == 4 and ones_digit == 0:
    print(numbers_in_english_tens["40"])
elif tens_digit == 4 and ones_digit == 1:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["1"])
elif tens_digit == 4 and ones_digit == 2:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["2"])
elif tens_digit == 4 and ones_digit == 3:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["3"])
elif tens_digit == 4 and ones_digit == 4:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["4"])
elif tens_digit == 4 and ones_digit == 5:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["5"])
elif tens_digit == 4 and ones_digit == 6:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["6"])
elif tens_digit == 4 and ones_digit == 7:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["7"])
elif tens_digit == 4 and ones_digit == 8:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["8"])
elif tens_digit == 4 and ones_digit == 9:
    print(numbers_in_english_tens["40"],'-',numbers_in_english_ones["9"])
elif tens_digit == 5 and ones_digit == 0:
    print(numbers_in_english_tens["50"])
elif tens_digit == 5 and ones_digit == 1:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["1"])
elif tens_digit == 5 and ones_digit == 2:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["2"])
elif tens_digit == 5 and ones_digit == 3:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["3"])
elif tens_digit == 5 and ones_digit == 4:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["4"])
elif tens_digit == 5 and ones_digit == 5:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["5"])
elif tens_digit == 5 and ones_digit == 6:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["6"])
elif tens_digit == 5 and ones_digit == 7:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["7"])
elif tens_digit == 5 and ones_digit == 8:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["8"])
elif tens_digit == 5 and ones_digit == 9:
    print(numbers_in_english_tens["50"],'-',numbers_in_english_ones["9"])
elif tens_digit == 6 and ones_digit == 0:
    print(numbers_in_english_tens["60"])
elif tens_digit == 6 and ones_digit == 1:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["1"])
elif tens_digit == 6 and ones_digit == 2:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["2"])
elif tens_digit == 6 and ones_digit == 3:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["3"])
elif tens_digit == 6 and ones_digit == 4:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["4"])
elif tens_digit == 6 and ones_digit == 5:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["5"])
elif tens_digit == 6 and ones_digit == 6:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["6"])
elif tens_digit == 6 and ones_digit == 7:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["7"])
elif tens_digit == 6 and ones_digit == 8:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["8"])
elif tens_digit == 6 and ones_digit == 9:
    print(numbers_in_english_tens["60"],'-',numbers_in_english_ones["9"])
elif tens_digit == 7 and ones_digit == 0:
    print(numbers_in_english_tens["70"])
elif tens_digit == 7 and ones_digit == 1:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["1"])
elif tens_digit == 7 and ones_digit == 2:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["2"])
elif tens_digit == 7 and ones_digit == 3:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["3"])
elif tens_digit == 7 and ones_digit == 4:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["4"])
elif tens_digit == 7 and ones_digit == 5:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["5"])
elif tens_digit == 7 and ones_digit == 6:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["6"])
elif tens_digit == 7 and ones_digit == 7:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["7"])
elif tens_digit == 7 and ones_digit == 8:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["8"])
elif tens_digit == 7 and ones_digit == 9:
    print(numbers_in_english_tens["70"],'-',numbers_in_english_ones["9"])
elif tens_digit == 8 and ones_digit == 0:
    print(numbers_in_english_tens["80"])
elif tens_digit == 8 and ones_digit == 1:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["1"])
elif tens_digit == 8 and ones_digit == 2:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["2"])
elif tens_digit == 8 and ones_digit == 3:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["3"])
elif tens_digit == 8 and ones_digit == 4:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["4"])
elif tens_digit == 8 and ones_digit == 5:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["5"])
elif tens_digit == 8 and ones_digit == 6:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["6"])
elif tens_digit == 8 and ones_digit == 7:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["7"])
elif tens_digit == 8 and ones_digit == 8:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["8"])
elif tens_digit == 8 and ones_digit == 9:
    print(numbers_in_english_tens["80"],'-',numbers_in_english_ones["9"])
elif tens_digit == 9 and ones_digit == 0:
    print(numbers_in_english_tens["90"])
elif tens_digit == 9 and ones_digit == 1:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["1"])
elif tens_digit == 9 and ones_digit == 2:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["2"])
elif tens_digit == 9 and ones_digit == 3:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["3"])
elif tens_digit == 9 and ones_digit == 4:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["4"])
elif tens_digit == 9 and ones_digit == 5:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["5"])
elif tens_digit == 9 and ones_digit == 6:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["6"])
elif tens_digit == 9 and ones_digit == 7:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["7"])
elif tens_digit == 9 and ones_digit == 8:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["8"])
elif tens_digit == 9 and ones_digit == 9:
    print(numbers_in_english_tens["90"],'-',numbers_in_english_ones["9"])
if hundred_digit == 1 and tens_digit == 0 and ones_digit == 0:
    print(number_in_english_hundreds["1"])
print(x)
print(hundred_digit,tens_digit,ones_digit)