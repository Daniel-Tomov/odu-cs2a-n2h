# Wireshark 4
## Challenges
Analyze the custom protocol in the packet capture. 
### Challenge 1
<details>
<summary>What is the flag?</summary>
How many messages were sent?
</details>
5
<details>
<summary>Walkthrough</summary>
Filter the packets by removing the ssh and http traffic.

```
tcp.port != 22 and not tcp.port eq 80
```

Here is the hexdump of the packets. The indented ones are from the server

```
00000000  00 00 00 05                                        ....
```

You can also tell by looking at the amount of repeating messages. 
</details>

### Challenge 2
<details>
<summary>What is the flag?</summary>
NCL-FJCG-1632
</details>

<details>
<summary>Walkthrough</summary>
Here is the hexdump of the packets. The indented ones are from the server

```
00000000  00 00 00 05                                        ....
00000004  04 17                                              ..
    00000000  00 00 00 a0                                        ....
00000006  00 00 00 58 54 6b 4e 4d  4c 55 5a 4b 51 30 63 74   ...XTkNM LUZKQ0ct
00000016  4d 54 59 7a 4d 69 42 4f  51 30 77 74 52 6b 70 44   MTYzMiBO Q0wtRkpD
00000026  52 79 30 78 4e 6a 4d 79  49 45 35 44 54 43 31 47   Ry0xNjMy IE5DTC1G
00000036  53 6b 4e 48 4c 54 45 32  4d 7a 49 67 54 6b 4e 4d   SkNHLTE2 MzIgTkNM
00000046  4c 55 5a 4b 51 30 63 74  4d 54 59 7a 4d 69 42 4f   LUZKQ0ct MTYzMiBO
00000056  0a 51 30 77 74 52 6b 70  44 52 79 30 04 17 00 00   .Q0wtRkp DRy0....
00000066  00 48 78 4e 6a 4d 79 49  45 35 44 54 43 31 47 53   .HxNjMyI E5DTC1GS
00000076  6b 4e 48 4c 54 45 32 4d  7a 49 67 54 6b 4e 4d 4c   kNHLTE2M zIgTkNML
00000086  55 5a 4b 51 30 63 74 4d  54 59 7a 4d 69 42 4f 51   UZKQ0ctM TYzMiBOQ
00000096  30 77 74 52 6b 70 44 52  79 30 78 4e 6a 4d 79 49   0wtRkpDR y0xNjMyI
000000A6  45 35 44 0a 54 43 31 47  53 6b 04 17 00 00 00 6b   E5D.TC1G Sk.....k
000000B6  4e 48 4c 54 45 32 4d 7a  49 67 54 6b 4e 4d 4c 55   NHLTE2Mz IgTkNMLU
000000C6  5a 4b 51 30 63 74 4d 54  59 7a 4d 69 42 4f 51 30   ZKQ0ctMT YzMiBOQ0
000000D6  77 74 52 6b 70 44 52 79  30 78 4e 6a 4d 79 49 45   wtRkpDRy 0xNjMyIE
000000E6  35 44 54 43 31 47 53 6b  4e 48 4c 54 45 32 4d 7a   5DTC1GSk NHLTE2Mz
000000F6  49 67 54 6b 4e 4d 0a 4c  55 5a 4b 51 30 63 74 4d   IgTkNM.L UZKQ0ctM
00000106  54 59 7a 4d 69 42 4f 51  30 77 74 52 6b 70 44 52   TYzMiBOQ 0wtRkpDR
00000116  79 30 78 4e 6a 4d 79 49  45 35 44 04 17 00 00 00   y0xNjMyI E5D.....
00000126  57 54 43 31 47 53 6b 4e  48 4c 54 45 32 4d 7a 49   WTC1GSkN HLTE2MzI
00000136  67 54 6b 4e 4d 4c 55 5a  4b 51 30 63 74 4d 54 59   gTkNMLUZ KQ0ctMTY
00000146  7a 4d 69 42 4f 51 30 77  74 0a 52 6b 70 44 52 79   zMiBOQ0w t.RkpDRy
00000156  30 78 4e 6a 4d 79 49 45  35 44 54 43 31 47 53 6b   0xNjMyIE 5DTC1GSk
00000166  4e 48 4c 54 45 32 4d 7a  49 67 54 6b 4e 4d 4c 55   NHLTE2Mz IgTkNMLU
00000176  5a 4b 51 30 63 74 4d 54  04 17 00 00 00 22 59 7a   ZKQ0ctMT ....."Yz
00000186  4d 69 42 4f 51 30 77 74  52 6b 70 44 52 79 30 78   MiBOQ0wt RkpDRy0x
00000196  4e 6a 4d 79 49 45 35 44  54 43 31 47 0a 53 6b 4e   NjMyIE5D TC1G.SkN
    00000004  b8 c9 7b 08 e1 98 fa 9f  f7 9a 3a 9c 1f 01 09 b1   ..{..... ..:.....
    00000014  86 87 b7 a1 a3 ff 17 72  c2 9b 4d c8 67 53 d7 11   .......r ..M.gS..
    00000024  88 17 15 3a e8 1d 94 b5  d6 c7 45 e6 3d 1d f3 1d   ...:.... ..E.=...
    00000034  5d 02 bd 3b 03 0b 82 0c  3c 03 86 54 fd ca 61 9c   ]..;.... <..T..a.
    00000044  f8 f9 e7 72 e1 d4 2c 5a  32 7c 0f ec 41 01 ec a5   ...r..,Z 2|..A...
    00000054  a2 7b 6d 93 b1 d2 10 2d  b5 a3 7e bd 52 e3 43 05   .{m....- ..~.R.C.
    00000064  f5 ef db dc fa 80 e9 c0  b9 af 15 5f 62 73 ba 99   ........ ..._bs..
    00000074  7c bd 3e 4a fd da d2 a9  50 df b9 f7 86 c5 64 f7   |.>J.... P.....d.
    00000084  6a 48 c4 29 5e f0 fa 5f  9b fe d8 28 3a 70 0b 63   jH.)^.._ ...(:p.c
    00000094  fe f2 05 46 86 e9 78 74  09 6b 1c 2b c0 d9 6e c4   ...F..xt .k.+..n.
```

Choose one of the base64 strings from the client and decode it. 
</details>