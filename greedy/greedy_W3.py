def construc(edges, total_nodes):  #ฟังก์ชันสร้าง adj list จากขอบของกราฟ
    adj = [[] for _ in range(total_nodes)]  #สร้างลิสต์เปล่าให้แต่ละโหนด เพื่อเก็บโหนดใกล้ที่สุด
    for u, v, wt in edges:  # วนลูปผ่านแต่ละขอบ (u = จุดเริ่ม, v = จุดปลาย, wt = น้ำหนัก)
        adj[u].append((v, wt))  #เพิ่มเพื่อนบ้าน v พร้อมน้ำหนัก ไปในโหนด u
        adj[v].append((u, wt))  #เพิ่มเพื่อนบ้าน u ไปในโหนด v ด้วย เพราะเป็นกราฟสองทาง
    return adj  #คืนค่า adj list ที่สร้างเสร็จแล้ว

def min_distance(dist, visited):  #ฟังก์ชันหาโหนดที่มีระยะทางน้อยสุดที่ยังไม่ถูกเยี่ยมชม
    min_val = float('inf')  # เริ่มจากตั้งค่าระยะต่ำสุดเป็นอนันต์
    min_index = -1  # ยังไม่พบ index ที่เหมาะสม
    for i in range(len(dist)):  # วนเช็คทุกโหนด
        if not visited[i] and dist[i] < min_val:  #ถ้ายังไม่เยี่ยมชมและระยะน้อยที่สุด
            min_val = dist[i]  #อัปเดตระยะต่ำสุด
            min_index = i  #เก็บ index ไว้
    return min_index  #คืนค่าหมายเลขโหนดที่ควรไปต่อ

def ress(total_nodes, edges, start, goal):  #ฟังก์ชันหาระยะทางสั้นสุด
    adj = construc(edges, total_nodes)  #สร้าง adj list จากข้อมูลขอบ
    dist = [float('inf')] * total_nodes  #สร้างลิสต์เก็บระยะห่างจากต้นทาง เริ่มเป็นอนันต์หมด
    visited = [False] * total_nodes  #เก็บสถานะว่าโหนดไหนถูกเยี่ยมชมแล้วบ้าง
    parent = [-1] * total_nodes  #เก็บว่าโหนดก่อนหน้าของแต่ละโหนดคืออะไร

    dist[start] = 0  #ระยะจาก start ไปยังตัวมันเองคือ 0

    for _ in range(total_nodes):  #วนลูปทั้งหมดเท่าจำนวนโหนด
        u = min_distance(dist, visited)  #หาโหนดที่มีระยะทางน้อยสุดที่ยังไม่ถูกเยี่ยมชม
        if u == -1:  #ถ้าไม่เจอให้เบรคออก
            break
        visited[u] = True  #ทำเครื่องหมายว่าโหนดนี้เคยมาแล้ว
        for v, weight in adj[u]:  #วนลูปดูเพื่อนบ้านของ u
            if not visited[v] and dist[v] > dist[u] + weight:  #ถ้ายังไม่เยี่ยมชมและมีทางที่สั้นกว่า
                dist[v] = dist[u] + weight  #อัปเดตระยะทางใหม่ให้สั้นลง
                parent[v] = u  #บันทึกเส้นทางว่า v มาจาก u

    # Reconstruct path
    path = []  #เตรียมลิสต์เก็บเส้นทาง
    cur = goal  #เริ่มจากปลายทาง
    while cur != -1:  #ย้อนกลับตาม parent ไปจนถึงต้นทาง
        path.append(cur)  #เพิ่มโหนดปัจจุบันเข้า path
        cur = parent[cur]  #ย้อนไปโหนดก่อนหน้า
    path.reverse()  #กลับลำดับจากหลังมาหน้า ให้เริ่มที่ start → goal

    return dist[goal], path  #คืนค่าระยะทางสั้นสุดและเส้นทางที่เดิน

if __name__ == "__main__":  #จุดเริ่มต้นของโปรแกรม
    start = 0  #โหนดเริ่มต้น
    goal = 5  #โหนดปลายทาง
    total_nodes = 9  #จำนวนโหนดทั้งหมดในกราฟ (0 ถึง 8)
    edges = [  #รายการขอบในกราฟ (เชื่อมระหว่างโหนด)
        [0, 1, 4],
        [0, 7, 8],
        [1, 7, 11],
        [1, 2, 8],
        [7, 8, 7],
        [7, 6, 1],
        [6, 8, 6],
        [8, 2, 2],
        [2, 5, 4],
        [2, 3, 7],
        [6, 5, 2],
        [3, 5, 14],
        [3, 4, 9],
        [5, 4, 10]
    ]

    cost, path = ress(total_nodes, edges, start, goal)
    print("ระยะทางรวมสั้นที่สุด:", cost)  
    print("เส้นทางที่ใช้:", " → ".join(map(str, path)))
