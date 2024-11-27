
# Sicherheitsmechanismen in ZB und IEEE

Sicherheitsstufe | Sicherheitsattribut | Datenverschlüsselung | Datenintegrität
-|-|-|-
0x00 | -            | aus   | nein (MIC = 0)
0x01 | MIC-32       | aus   | ja (MIC = 4)
0x02 | MIC-64       | aus   | ja (MIC = 8)
0x03 | MIC-128      | aus   | ja (MIC = 16)
0x04 | ENC          | an    | nein (MIC = 0)
0x05 | ENC-MIC-32   | an    | ja (MIC = 4)
0x06 | ENC-MIC-64   | an    | ja (MIC = 8)
0x07 | ENC-MIC-128  | an    | ja (MIC = 16)



