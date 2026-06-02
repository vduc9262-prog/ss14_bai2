# Tổng điểm hiện tại của khách hàng
total_points = 100


# Hàm cộng điểm thưởng
def add_reward_points(current_points, points_earned):
    return current_points + points_earned


# Khách được thưởng thêm 50 điểm
total_points = add_reward_points(total_points, 50)

print("Đã cộng thêm 50 điểm.")
print("Tổng điểm hiện tại của khách hàng:", total_points)




#  total_points là biến global vì được khai báo bên ngoài hàm.

#  Python coi total_points trong hàm là biến local do có phép gán total_points = ..., nhưng biến này chưa có giá trị nên báo lỗi UnboundLocalError.

#  Không lỗi, vì Python cho phép đọc biến global bên trong hàm.

#  Dùng từ khóa:

# global total_points

#  Dùng lệnh return để trả về tổng điểm mới từ hàm.
