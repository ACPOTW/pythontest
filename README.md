# pythontest

开发内容

1. python测试
  1. scrapy爬取测试
    1. 通过 scrapy 实现网页信息爬取和采集。
    2. 通过提供的列表页网址采集到详情页的信息。
    3. 爬取结果存成一份 JSON文档。
    4. JSON文档要求： 主要信息（标题（title） 价格(price) 颜色(color) 尺码(size) 网站货号(sku) 详情(details) 大图的URL (img_urls)，其它字段随意
    5. 要爬取的地址
     1. 网站 https://jd.com/
        列表页网址 https://list.jd.com/list.html?cat=1318,12099,9756

  2. 将如下网页渲染后的内容保存为图片
    1. 5分钟保存一次
    2. 图片名称中包含保存的时间戳
    3. 网站地址
      1. https://www.163.com/
    
  3. 算法
    1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
      Example1:
      Input: nums = [2,7,11,15], target = 9
      Output: [0,1]
      Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
      Constraints:
      2 <= nums.length <= 104
      -109 <= nums[i] <= 109
      -109 <= target <= 109
      Only one valid answer exists.

    2. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
      Example1
      Input: nums1 = [1,3], nums2 = [2]
      Output: ‪2.00000‬
      Explanation: merged array = [1,2,3] and median is 2.
      Constraints:
      nums1.length == m
      nums2.length == n
      0 <= m <= 1000
      0 <= n <= 1000
      1 <= m + n <= 2000
      -106 <= nums1[i], nums2[i] <= 106

2. linux    
  1. 编写一个shell脚本(linux)，功能如下
  在给定文件中搜索指定内容，并将搜索结果(含内容出现的行号)保存到新的文件中，同时结果输出到控制台
  2. 编写一个shell: 显示当前硬盘使用情况，内存使用情况，CPU使用情况

3. 学生管理系统:
   根据原型完成学生管理系统，使用java或者ruby on rails任意一个，数据库使用mysql
   原型地址https://qnbc60.axshare.com/#id=qf3yyi&p=login
   1. java可使用springboot或java web
   5. ruby 使用rails完成用户的CRUD(建议使用linux系统或者wsl)https://guides.rubyonrails.org/getting_started.html