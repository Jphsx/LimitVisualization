import re

TestCategories=["Ch0L_0_2j0bS_ge1jge1bISR_PTISR1_gamT1","Ch1L_mum_gold_0j0svS_ge1j0bISR_PTISR1","Ch2L_Zstar_gold_ge2jge1bS_ge1jge1bISR_PTISR0_gamT0"]


T2ttGrid=[
"4000390",
"4000370",
"4000350",
"4000330",
"6000590",
"6000570",
"6000550",
"6000530",
"8000790",
"8000770",
"8000750",
"8000730",
"10000990",
"10000970",
"10000950",
"10000930"
]

TChiWZGrid=[
"2000195",
"2000190",
"2000180",
"2000160", 
"3000295", 
"3000290",
"3000280", 
"3000260", 
"4000395", 
"4000390", 
"4000380", 
"4000360",
]

LJdict={
"Ch0L_0jS":".*0L.*.*0j.*S_.*",
"Ch0L_1jS":".*0L.*.*1j.*S_.*",
"Ch0L_2jS":".*0L.*.*2j.*S_.*",
"Ch0L_3jS":".*0L.*.*3j.*S_.*",
"Ch0L_4jS":".*0L.*.*4j.*S_.*",
"Ch0L_5jS":".*0L.*.*5j.*S_.*",
"Ch1L_0jS":".*1L.*.*0j.*S_.*",
"Ch1L_1jS":".*1L.*.*1j.*S_.*",
"Ch1L_2jS":".*1L.*.*2j.*S_.*",
"Ch1L_3jS":".*1L.*.*3j.*S_.*",
"Ch1L_4jS":".*1L.*.*4j.*S_.*",
"Ch2L_0jS":".*2L.*.*0j.*S_.*",
"Ch2L_1jS":".*2L.*.*1j.*S_.*",
"Ch2L_2jS":".*2L.*.*2j.*S_.*",
"Ch3L_0jS":".*3L.*.*0j.*S_.*",
"Ch3L_1jS":".*3L.*.*1j.*S_.*"
}


Categories=[
"Ch0L_0_0j1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch0L_0_0j1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch0L_0_1j0b0svS_ge1j0bISR_PTISR0", 
"Ch0L_0_1j0b0svS_ge1j0bISR_PTISR1", 
"Ch0L_0_1j0b0svS_ge1jge1bISR_PTISR0", 
"Ch0L_0_1j0b0svS_ge1jge1bISR_PTISR1", 
"Ch0L_0_1j1b0svS_ge1j0bISR_PTISR0", 
"Ch0L_0_1j1b0svS_ge1j0bISR_PTISR1", 
"Ch0L_0_1j1b0svS_ge1jge1bISR_PTISR0", 
"Ch0L_0_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch0L_0_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch0L_0_2j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_2j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch0L_0_2j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_2j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch0L_0_2j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch0L_0_2j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch0L_0_2j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_2j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch0L_0_2j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_2j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch0L_0_2j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_2j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch0L_0_2j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch0L_0_2j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch0L_0_2j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_2j2bS_ge1jISR_PTISR0_gamT0", 
"Ch0L_0_2j2bS_ge1jISR_PTISR0_gamT1", 
"Ch0L_0_3j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_3j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch0L_0_3j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_3j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch0L_0_3j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch0L_0_3j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch0L_0_3j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_3j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch0L_0_3j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_3j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch0L_0_3j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_3j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch0L_0_3j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch0L_0_3j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch0L_0_3jge2bS_ge1jISR_PTISR1_gamT1", 
"Ch0L_0_4j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_4j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch0L_0_4j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_4j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch0L_0_4j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch0L_0_4j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch0L_0_4j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_4j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch0L_0_4j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_4jge2bS_ge1jISR_PTISR0_gamT0", 
"Ch0L_0_4jge2bS_ge1jISR_PTISR1_gamT0", 
"Ch0L_0_ge5j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_ge5j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_ge5j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch0L_0_ge5j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch0L_0_ge5jge2bS_ge1jISR_PTISR1_gamT0", 
"Ch1L_elm_gold_0j0svS_ge1j0bISR_PTISR0", 
"Ch1L_elm_gold_0j0svS_ge1j0bISR_PTISR1", 
"Ch1L_elm_gold_0j0svS_ge1jge1bISR_PTISR0", 
"Ch1L_elm_gold_0j0svS_ge1jge1bISR_PTISR1", 
"Ch1L_elp_gold_0j0svS_ge1j0bISR_PTISR0", 
"Ch1L_elp_gold_0j0svS_ge1j0bISR_PTISR1", 
"Ch1L_elp_gold_0j0svS_ge1jge1bISR_PTISR0", 
"Ch1L_elp_gold_0j0svS_ge1jge1bISR_PTISR1", 
"Ch1L_elpm_bron_0j0svS_ge1jISR_PTISR0", 
"Ch1L_elpm_bron_0j0svS_ge1jISR_PTISR1", 
"Ch1L_elpm_bron_1j0svS_ge1jISR_PTISR0", 
"Ch1L_elpm_bron_1j0svS_ge1jISR_PTISR1", 
"Ch1L_elpm_bron_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_elpm_bron_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_elpm_bron_2jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_elpm_bron_2jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_elpm_bron_2jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_elpm_bron_2jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_elpm_bron_3jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_elpm_bron_3jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_elpm_bron_3jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_elpm_bron_3jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_elpm_bron_ge4jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_elpm_bron_ge4jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_elpm_slvr_0j0svS_ge1jISR_PTISR0", 
"Ch1L_elpm_slvr_0j0svS_ge1jISR_PTISR1", 
"Ch1L_elpm_slvr_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_elpm_slvr_1j0svS_ge1jISR_PTISR0", 
"Ch1L_elpm_slvr_1j0svS_ge1jISR_PTISR1", 
"Ch1L_elpm_slvr_2jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_elpm_slvr_2jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_elpm_slvr_2jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_elpm_slvr_2jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_elpm_slvr_3jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_elpm_slvr_3jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_elpm_slvr_3jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_elpm_slvr_3jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_elpm_slvr_ge4jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_elpm_slvr_ge4jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_elpm_slvr_ge4jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_lm_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_lm_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_lpm_gold_1j0b0svS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_1j0b0svS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_1j0b0svS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_1j0b0svS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_1j0b0svS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_1j0b0svS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_1j0b0svS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_1j0b0svS_ge1jge1bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_1j1b0svS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_1j1b0svS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_1j1b0svS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_1j1b0svS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_1j1b0svS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_1j1b0svS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_1j1b0svS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_lpm_gold_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_lpm_gold_2j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_2j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_2j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_2j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_2j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_2j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_2j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_2j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_2j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_2j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_2j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_2j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_2j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_2j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_2j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_2j2bS_ge1jISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_2j2bS_ge1jISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_3j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_3j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_3j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_3j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_3j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_3j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_3j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_3j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_3j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_3j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_3j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_3j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_3j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_3jge2bS_ge1jISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_3jge2bS_ge1jISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_3jge2bS_ge1jISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_ge4j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_ge4j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_ge4j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_ge4j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_ge4j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_ge4j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_ge4j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_ge4j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_ge4j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_ge4j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_ge4jge2bS_ge1jISR_PTISR0_gamT0", 
"Ch1L_mum_gold_0j0svS_ge1j0bISR_PTISR0", 
"Ch1L_mum_gold_0j0svS_ge1j0bISR_PTISR1", 
"Ch1L_mum_gold_0j0svS_ge1jge1bISR_PTISR0", 
"Ch1L_mum_gold_0j0svS_ge1jge1bISR_PTISR1", 
"Ch1L_mup_gold_0j0svS_ge1j0bISR_PTISR0", 
"Ch1L_mup_gold_0j0svS_ge1j0bISR_PTISR1", 
"Ch1L_mup_gold_0j0svS_ge1jge1bISR_PTISR0", 
"Ch1L_mup_gold_0j0svS_ge1jge1bISR_PTISR1", 
"Ch1L_mupm_bron_0j0svS_ge1jISR_PTISR0", 
"Ch1L_mupm_bron_0j0svS_ge1jISR_PTISR1", 
"Ch1L_mupm_bron_1j0svS_ge1jISR_PTISR0", 
"Ch1L_mupm_bron_1j0svS_ge1jISR_PTISR1", 
"Ch1L_mupm_bron_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_mupm_bron_2jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_mupm_bron_2jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_mupm_bron_2jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_mupm_bron_2jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_mupm_bron_3jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_mupm_bron_3jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_mupm_bron_3jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_mupm_bron_3jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_mupm_bron_ge4jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_mupm_bron_ge4jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_mupm_bron_ge4jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_mupm_slvr_0j0svS_ge1jISR_PTISR0", 
"Ch1L_mupm_slvr_0j0svS_ge1jISR_PTISR1", 
"Ch1L_mupm_slvr_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_mupm_slvr_1j0svS_ge1jISR_PTISR0", 
"Ch1L_mupm_slvr_1j0svS_ge1jISR_PTISR1", 
"Ch1L_mupm_slvr_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_mupm_slvr_2jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_mupm_slvr_2jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_mupm_slvr_2jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_mupm_slvr_2jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_mupm_slvr_3jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_mupm_slvr_3jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_mupm_slvr_3jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_mupm_slvr_3jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_mupm_slvr_ge4jS_ge1jISR_PTISR0_gamT0", 
"Ch1L_mupm_slvr_ge4jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_mupm_slvr_ge4jS_ge1jISR_PTISR1_gamT0", 
"Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_OSelel_gold_0j0svS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_OSelel_gold_0j0svS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_OSelel_gold_0j0svS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_OSelel_gold_0j0svS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_OSelel_gold_0j0svS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_OSelmu_gold_0j0svS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_OSelmu_gold_0j0svS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_OSelmu_gold_0j0svS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_OSelmu_gold_0j0svS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_OSelmu_gold_0j0svS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_OSelmu_gold_0j0svS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_OSelmu_gold_0j0svS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_OSelmu_gold_0j0svS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_OSmumu_gold_0j0svS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_OSmumu_gold_0j0svS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_OSmumu_gold_0j0svS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_OSmumu_gold_0j0svS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_OSmumu_gold_0j0svS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_SS_gold_0j0svS_ge1jISR_PTISR0", 
"Ch2L_SS_gold_1jS_ge1jISR_PTISR0", 
"Ch2L_SS_gold_ge2jS_ge1jISR_PTISR0", 
"Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_Zstar_gold_1j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_1j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_Zstar_gold_1j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_Zstar_gold_1j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_Zstar_gold_1j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_1j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_Zstar_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_ge2j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_Zstar_gold_ge2j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_Zstar_gold_ge2j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_elel_bron_0j0svS_ge1jISR_PTISR0", 
"Ch2L_elel_bron_1jS_ge1jISR_PTISR0", 
"Ch2L_elel_bron_ge2jS_ge1jISR_PTISR0", 
"Ch2L_elel_slvr_0j0svS_ge1jISR_PTISR0", 
"Ch2L_elel_slvr_1jS_ge1jISR_PTISR0", 
"Ch2L_elel_slvr_ge2jS_ge1jISR_PTISR0", 
"Ch2L_elmu_bron_0j0svS_ge1jISR_PTISR0", 
"Ch2L_elmu_bron_1jS_ge1jISR_PTISR0", 
"Ch2L_elmu_bron_ge2jS_ge1jISR_PTISR0", 
"Ch2L_elmu_slvr_0j0svS_ge1jISR_PTISR0", 
"Ch2L_elmu_slvr_1jS_ge1jISR_PTISR0", 
"Ch2L_elmu_slvr_ge2jS_ge1jISR_PTISR0", 
"Ch2L_ll_bron_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch2L_ll_bron_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch2L_ll_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch2L_ll_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch2L_ll_slvr_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch2L_ll_slvr_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch2L_mumu_bron_0j0svS_ge1jISR_PTISR0", 
"Ch2L_mumu_bron_1jS_ge1jISR_PTISR0", 
"Ch2L_mumu_bron_ge2jS_ge1jISR_PTISR0", 
"Ch2L_mumu_slvr_0j0svS_ge1jISR_PTISR0", 
"Ch2L_mumu_slvr_1jS_ge1jISR_PTISR0", 
"Ch2L_mumu_slvr_ge2jS_ge1jISR_PTISR0", 
"Ch2L_noZ_gold_1j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_1j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_1j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_noZ_gold_1j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_1j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_1j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_1j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_noZ_gold_1j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_1j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_1j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_1j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_noZ_gold_1j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_1j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_noZ_gold_ge2j0bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_ge2j0bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_noZ_gold_ge2j0bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_ge2j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_ge2j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_ge2j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_noZ_gold_ge2j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_ge2jge1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_ge2jge1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_ge2jge1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_noZ_gold_ge2jge1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_ge2jge1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch3L_Zstar_bron_0jS_ge1jISR_PTISR0", 
"Ch3L_Zstar_bron_ge1jS_ge1jISR_PTISR0", 
"Ch3L_Zstar_gold_ge1jS_ge1jISR_PTISR0", 
"Ch3L_Zstar_slvr_0jS_ge1jISR_PTISR0", 
"Ch3L_Zstar_slvr_ge1jS_ge1jISR_PTISR0", 
"Ch3L_noZ_bron_0jS_ge1jISR_PTISR0", 
"Ch3L_noZ_bron_ge1jS_ge1jISR_PTISR0", 
"Ch3L_noZ_gold_0jS_ge1jISR_PTISR0", 
"Ch3L_noZ_slvr_0jS_ge1jISR_PTISR0", 
"Ch3L_noZ_slvr_ge1jS_ge1jISR_PTISR0", 
"Ch0L_0_1j1b0svS_ge1jge1bISR_PTISR1", 
"Ch0L_0_2j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch0L_0_2j2bS_ge1jISR_PTISR1_gamT0", 
"Ch0L_0_2j2bS_ge1jISR_PTISR1_gamT1", 
"Ch0L_0_3j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_3jge2bS_ge1jISR_PTISR0_gamT0", 
"Ch0L_0_3jge2bS_ge1jISR_PTISR0_gamT1", 
"Ch0L_0_3jge2bS_ge1jISR_PTISR1_gamT0", 
"Ch0L_0_4j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_4j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch0L_0_4j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_4jge2bS_ge1jISR_PTISR0_gamT1", 
"Ch0L_0_ge5j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch0L_0_ge5j0bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_ge5j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch0L_0_ge5j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_ge5jge2bS_ge1jISR_PTISR0_gamT0", 
"Ch1L_elpm_bron_ge4jS_ge1jISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_2j2bS_ge1jISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_1j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch3L_SS_bron_inclS_ge1jISR_PTISR0", 
"Ch3L_Zstar_gold_0jS_ge1jISR_PTISR0", 
"Ch3L_noZ_gold_ge1jS_ge1jISR_PTISR0", 
"Ch0L_0_3j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch0L_0_4j0bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch0L_0_4j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch0L_0_4j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_elpm_bron_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_elpm_bron_ge4jS_ge1jISR_PTISR0_gamT1", 
"Ch1L_elpm_slvr_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_elpm_slvr_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_lp_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_lp_gold_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_lpm_gold_2j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_2j2bS_ge1jISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_3j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_3j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_3jge2bS_ge1jISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_ge4j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_ge4j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch1L_mupm_bron_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_mupm_bron_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_mupm_slvr_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_mupm_slvr_1jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_mupm_slvr_ge4jS_ge1jISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_1j1bS_ge1j0bISR_PTISR0_gamT0", 
"Ch2L_Zstar_gold_1j1bS_ge1j0bISR_PTISR1_gamT0", 
"Ch2L_Zstar_gold_1j1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_Zstar_gold_1j1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch2L_Zstar_gold_ge2j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_1j1b0svS_ge1jge1bISR_PTISR1_gamT1", 
"Ch0L_0_4jge2bS_ge1jISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_1j1bS_ge1j0bISR_PTISR0_gamT1", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1jge1bISR_PTISR1_gamT0", 
"Ch0L_0_4j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch1L_elpm_bron_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_elpm_slvr_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch1L_elpm_slvr_ge4jS_ge1jISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_3j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch1L_lpm_gold_ge4j0bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_ge4j0bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_ge4j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_ge4jge2bS_ge1jISR_PTISR0_gamT1", 
"Ch1L_lpm_gold_ge4jge2bS_ge1jISR_PTISR1_gamT0", 
"Ch1L_lpm_gold_ge4jge2bS_ge1jISR_PTISR1_gamT1", 
"Ch1L_mupm_bron_0jge1svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch1L_mupm_bron_ge4jS_ge1jISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch2L_noZ_gold_ge2jge1bS_ge1jge1bISR_PTISR0_gamT0", 
"Ch1L_lpm_gold_ge4j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_1j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_ge2jge1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch0L_0_0jge2svS_ge1jISR_PTISR0_gamT0_SVeta0", 
"Ch0L_0_0jge2svS_ge1jISR_PTISR0_gamT0_SVeta1", 
"Ch2L_Zstar_gold_1j1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch2L_noZ_gold_1j1bS_ge1j0bISR_PTISR1_gamT1", 
"Ch2L_noZ_gold_ge2jge1bS_ge1jge1bISR_PTISR0_gamT1", 
"Ch3L_SS_slvr_inclS_ge1jISR_PTISR0", 
"Ch3L_SS_gold_inclS_ge1jISR_PTISR0", 
"Ch2L_Zstar_gold_1j1bS_ge1jge1bISR_PTISR1_gamT1", 
"Ch2L_Zstar_gold_ge2jge1bS_ge1jge1bISR_PTISR1_gamT1"]

print("Total Categories: ",len(Categories))


def getMaskListDict(regexdict, catlist):
	maskDict={}
	for task in regexdict:
		matching_elements = [element for element in catlist if re.match(regexdict[task], element)]	
		maskDict[task] = matching_elements
		
	return maskDict
