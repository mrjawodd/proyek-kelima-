import time
import random


def slow_print(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def game_utama():
    slow_print("--- MEMULAI PETUALANGAN DIGITAL ---\n")
    nama = input("Siapa namamu, pahlawan? ")
    slow_print(f"Selamat datang, {nama}. Desa Sunyi sedang ditimpa teror.")
    slow_print("Tugasmu: menumpas para penjahat dan membebaskan masyarakat yang tak bersalah.")

    slow_print("Di hadapanmu ada dua jalur untuk mencapai pusat kejahatan:")
    slow_print("1) Lembah Coding — sebuah lembah dengan jebakan logika dan para peretas licik.")
    slow_print("2) Gunung Bug — puncak penuh makhluk aneh yang menyebabkan program kacau.")

    pilihan = input("Pilih jalurmu (ketik 'Lembah Coding' atau 'Gunung Bug'): ").strip().lower()

    def battle(enemy_name, enemy_hp, player_hp, rations, max_player_hp=20):
        slow_print(f"Pertarungan dimulai melawan {enemy_name}!")
        defending = False
        while enemy_hp > 0 and player_hp > 0:
            slow_print(f"HP kamu: {player_hp}/{max_player_hp} | HP {enemy_name}: {enemy_hp} | Makanan tersisa: {rations}")
            action = input("Pilih tindakan (attack/defend/flee/eat atau makan): ").strip().lower()
            if action == "attack" or action == "serang":
                dmg = random.randint(4, 8)
                enemy_hp -= dmg
                slow_print(f"Kamu menyerang dan memberi {dmg} damage.")
                defending = False
            elif action == "defend" or action == "lindung":
                slow_print("Kau mengangkat perisai dan bersiap menahan serangan.")
                defending = True
            elif action == "flee":
                if random.random() < 0.5:
                    slow_print("Berhasil kabur dari pertarungan!")
                    return False, player_hp, rations
                else:
                    slow_print("Gagal kabur! Musuh menyerang kesempatan itu.")
                    defending = False
            elif action == "eat" or action == "makan":
                if rations > 0:
                    heal = random.randint(4, 8)
                    old_hp = player_hp
                    player_hp = min(max_player_hp, player_hp + heal)
                    rations -= 1
                    slow_print(f"Kau makan dan memulihkan {player_hp - old_hp} HP. Makanan tersisa: {rations}.")
                    defending = False
                else:
                    slow_print("Kau tidak punya makanan lagi!")
                    defending = False
            else:
                slow_print("Pilihan tidak valid — kesempatan terbuka untuk musuh.")
                defending = False

            if enemy_hp > 0:
                enemy_dmg = random.randint(2, 6)
                if defending:
                    enemy_dmg = max(1, enemy_dmg - 2)
                player_hp -= enemy_dmg
                slow_print(f"{enemy_name} menyerang dan memberi {enemy_dmg} damage.")

        if player_hp > 0:
            slow_print(f"Kau menang melawan {enemy_name}! (Sisa HP: {player_hp})")
            return True, player_hp, rations
        else:
            slow_print("Kau kalah dalam pertarungan...")
            return False, player_hp, rations

    max_player_hp = 20
    player_hp = max_player_hp
    rations = 2

    if pilihan == "lembah coding" or pilihan == "1":
        slow_print("Kau memasuki Lembah Coding. Kabut berisi baris-baris kode bergelung.")
        slow_print("Tiba-tiba sekelompok 'Bug Thief' muncul dan mencoba mengacak program desa.")
        won, player_hp, rations = battle("Bug Thief Squad", 12, player_hp, rations, max_player_hp)
        if won:
            slow_print("Dengan kecerdasan dan refactor cepat, kau mengalahkan para peretas!")
            slow_print("Desa aman kembali. Rakyat bersorak karena logika yang terkoreksi.")
            istirahat = input("Ingin istirahat di rumah warga untuk memulihkan HP? (y/n): ").strip().lower()
            if istirahat == "y" or istirahat == "ya":
                slow_print("Warga menyambutmu, memberi tempat tidur dan lauk. HP pulih penuh.")
                player_hp = max_player_hp
                rations += 2
                slow_print(f"HPmu pulih menjadi {player_hp}. Makanan bertambah menjadi {rations}.")
            lanjut = input("Kembali sebagai ksatria untuk melawan Pangeran? (y/n): ").strip().lower()
            if lanjut == "y" or lanjut == "ya":
                slow_print("Kau menuju ke istana, diselimuti aura gelap. Siap menghadapi Pangeran.")
                won_final, player_hp, rations = battle("Pangeran Korupsi", 22, player_hp, rations, max_player_hp)
                if won_final:
                    slow_print("Kau mengalahkan Pangeran! Desa bebas dari teror selamanya.")
                else:
                    slow_print("Pertarungan melawan Pangeran terlalu keras — kau harus pulih dan kembali lagi nanti.")
        else:
            slow_print("Kekacauan sempat terjadi — beberapa sistem rusak, dan kau perlu pulih.")

    elif pilihan == "gunung bug" or pilihan == "2":
        slow_print("Kau menapaki Gunung Bug. Angin membawa bisikan error.")
        slow_print("Seekor 'Giant Null' menghadang dan mencoba menelan variabel-variabel penting.")
        won, player_hp, rations = battle("Giant Null", 14, player_hp, rations, max_player_hp)
        if won:
            slow_print("Dengan keberanian, kau menambal lubang memori dan menundukkan Giant Null.")
            slow_print("Para penduduk berterima kasih karena layanan mereka pulih.")
            istirahat = input("Ingin istirahat di rumah warga untuk memulihkan HP? (y/n): ").strip().lower()
            if istirahat == "y" or istirahat == "ya":
                slow_print("Warga menyambutmu, memberi tempat tidur dan lauk. HP pulih penuh.")
                player_hp = max_player_hp
                rations += 2
                slow_print(f"HPmu pulih menjadi {player_hp}. Makanan bertambah menjadi {rations}.")
            lanjut = input("Kembali sebagai ksatria untuk melawan Pangeran? (y/n): ").strip().lower()
            if lanjut == "y" or lanjut == "ya":
                slow_print("Kau menuju ke istana, diselimuti aura gelap. Siap menghadapi Pangeran.")
                won_final, player_hp, rations = battle("Pangeran Korupsi", 22, player_hp, rations, max_player_hp)
                if won_final:
                    slow_print("Kau mengalahkan Pangeran! Desa bebas dari teror selamanya.")
                else:
                    slow_print("Pertarungan melawan Pangeran terlalu keras — kau harus pulih dan kembali lagi nanti.")
        else:
            slow_print("Pertarungan berat — kau terluka, namun berhasil menyingkirkan ancaman itu secara sementara.")
            slow_print("Kau harus kembali lagi nanti untuk memastikan perdamaian.")

    else:
        slow_print("Pilihan tidak dikenali. Musuh memanfaatkan kebingunganmu dan kabur.")
        slow_print("Cobalah lagi dan pilih salah satu jalur yang tersedia.")

    slow_print("Terima kasih telah bermain. Sampai jumpa di petualangan berikutnya!")


if __name__ == "__main__":
    game_utama()