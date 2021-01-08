\ENCODING=ISO-8859-1
\Problem name: 

Minimize
 obj: Highest_e
Subject To
 coalition1110: - x_G1 - x_G2 - x_D1 - Highest_e <= -2720
 coalition1101: - x_G1 - x_G2 - x_D2 - Highest_e <= -1150
 coalition1011: - x_G1 - x_D1 - x_D2 - Highest_e <= -2520
 coalition0111: - x_G2 - x_D1 - x_D2 - Highest_e <= -1600
 coalition1100: - x_G1 - x_G2 - Highest_e <= 0
 coalition1010: - x_G1 - x_D1 - Highest_e <= -2520
 coalition1001: - x_G1 - x_D2 - Highest_e <= -1150
 coalition0110: - x_G2 - x_D1 - Highest_e <= -1600
 coalition0101: - x_G2 - x_D2 - Highest_e <= -750
 coalition0011: - x_D1 - x_D2 - Highest_e <= 0
 coalition1000: - x_G1 - Highest_e <= 0
 coalition0100: - x_G2 - Highest_e <= 0
 coalition0010: - x_D1 - Highest_e <= 0
 coalition0001: - x_D2 - Highest_e <= 0
 balance:       x_G1 + x_G2 + x_D1 + x_D2  = 3470
Bounds
      Highest_e Free
End
