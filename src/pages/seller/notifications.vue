<route lang="yaml">
meta:
  layout: seller/LSDashBoard
</route>

<script setup>
useHead({
  title: 'seller | notifications',
})
const notifications = reactive([{
  img: '/img/gen/notif-1.jpg',
  title: 'shoper Xu sắp hết hạn!!',
  desc: 'Bạn đang có 300 shoper Xu sẽ hết hạn vào ngày 28-02-2022. Mua hàng và sử dụng ngay nào!',
  time: '19:00 22/02/2022',
}, {
  img: '/img/gen/notif-2.jpg',
  title: 'thuongtruong1009 ơi! Deal HOT giá 9K đang chờ',
  desc: '😍 Giá giảm sốc chỉ từ 9K ✨ Sản phẩm từ tất cả ngành hàng ☄️ Áp thêm mã Voucher cực HOT 💥 Còn chờ chi? Mua ngay đi',
  time: '19:00 22/02/2022',
},
{
  img: '/img/gen/notif-3.jpg',
  title: 'Nhiều phần thưởng hấp dẫn đang chờ bạn 🤩!',
  desc: 'Hoàn thành Nhiệm vụ Người bán để rinh về nhiều phần thưởng giá trị và thúc đẩy bùng nổ doanh số bán hàng cho Shop 💪🏻. Tham gia NGAY! >>',
  time: '19:00 22/02/2022',
},
{
  img: '/img/gen/notif-4.jpg',
  title: 'Thu cũ đổi mới - Lên đời Samsung S22',
  desc: 'Tạm biệt "dế" cũ - tậu ngay "dế" mới tại shoper. ⚡ Đặc biệt từ 11.02 đến 03.03, bạn sẽ nhận ngay ưu đãi độc quyền 🌟 7.000.000đ 🌟 từ Samsung 🔥 Tham gia ngay kẻo lỡ!',
  time: '19:00 22/02/2022',
},
{
  img: '/img/gen/notif-5.jpg',
  title: 'Bí quyết \"2-KHÔNG-2-CÓ\"',
  desc: '⛔ KHÔNG NÊN: - Nhận hàng có mã đơn lạ. - Nhận quà không rõ chương trình/có thu thêm phí. 😊 NÊN: - Nhận hàng có ghi rõ mã đơn đã đặt trên shoper. - Nhận quà từ chương trình đã tham gia. Xem bí quyết kiểm tra, nhận hàng chuẩn TẠI ĐÂY',
  time: '19:00 22/02/2022',
},
{
  img: '/img/gen/notif-2.jpg',
  title: 'thuongtruong1009 ơi! Deal HOT giá 9K đang chờ',
  desc: '😍 Giá giảm sốc chỉ từ 9K ✨ Sản phẩm từ tất cả ngành hàng ☄️ Áp thêm mã Voucher cực HOT 💥 Còn chờ chi? Mua ngay đi',
  time: '19:00 22/02/2022',
},
{
  img: '/img/gen/notif-2.jpg',
  title: 'thuongtruong1009 ơi! Deal HOT giá 9K đang chờ',
  desc: '😍 Giá giảm sốc chỉ từ 9K ✨ Sản phẩm từ tất cả ngành hàng ☄️ Áp thêm mã Voucher cực HOT 💥 Còn chờ chi? Mua ngay đi',
  time: '19:00 22/02/2022',
}])

</script>

<template>
  <div class="seller-notifications-container max-w-272 w-272 px-5 bg-white shadow-sm shadow-gray-500/50 rounded-2xl divide-y divide-solid divide-1 divide-light-800">
    <div class="flex justify-between items-center py-5">
      <h1 class="text-xl font-medium flex items-center gap-2">
        <INotify class="text-xl" />All notifications
      </h1>
      <div class="hover:bg-[#F6F6F6] rounded-md border-1 border-solid border-gray-300 py-1 px-5 cursor-pointer">
        <p class="flex items-center gap-2">
          <IMark />mark read all
        </p>
      </div>
    </div>
    <div v-for="(notify, i) in notifications" :key="i" class="py-2 flex items-start gap-4">
      <img :src="notify.img" alt="notify_img" class="max-w-10 max-h-10 rounded-md cursor-pointer">
      <div>
        <div class="hover:text-[#2673DD] cursor-pointer duration-200">
          <h6 class="font-medium">
            {{ notify.title }}
          </h6>
          <p class="text-sm">
            {{ notify.desc }}
          </p>
        </div>
        <p class="text-xs font-normal text-gray-400">
          {{ notify.time }}
        </p>
      </div>
    </div>
  </div>
</template>
