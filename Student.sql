-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- 主机： localhost:3306
-- 生成日期： 2022-12-20 16:53:41
-- 服务器版本： 8.0.31-0ubuntu0.20.04.1
-- PHP 版本： 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `Student`
--

-- --------------------------------------------------------

--
-- 表的结构 `api_administrator`
--

CREATE TABLE `api_administrator` (
  `administrator` int NOT NULL,
  `administrator_name` varchar(64) NOT NULL,
  `administrator_departments_id` int NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `mail` varchar(254) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_administrator`
--

INSERT INTO `api_administrator` (`administrator`, `administrator_name`, `administrator_departments_id`, `password`, `mail`) VALUES
(10070, '计算机', 1007, 'e0358d424529506847b22b747a3cb825', 'zhao2073981548@163.com'),
(10240, '测绘', 1024, 'e0358d424529506847b22b747a3cb825', 'zhao2073981548@163.com');

-- --------------------------------------------------------

--
-- 表的结构 `api_class`
--

CREATE TABLE `api_class` (
  `classID` int NOT NULL,
  `class_name` varchar(255) NOT NULL,
  `professional_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_class`
--

INSERT INTO `api_class` (`classID`, `class_name`, `professional_id`) VALUES
(6, '网络2031班', 8),
(12, '网络2032班', 8),
(13, '信息安全2001班', 15),
(14, '通信2030班', 12);

-- --------------------------------------------------------

--
-- 表的结构 `api_class_course`
--

CREATE TABLE `api_class_course` (
  `id` bigint NOT NULL,
  `classid_id` int NOT NULL,
  `course_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_class_course`
--

INSERT INTO `api_class_course` (`id`, `classid_id`, `course_id`) VALUES
(15, 6, 6),
(22, 6, 5),
(23, 6, 12),
(24, 6, 13),
(25, 6, 14);

-- --------------------------------------------------------

--
-- 表的结构 `api_courses`
--

CREATE TABLE `api_courses` (
  `course` int NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `course_credits` int NOT NULL,
  `course_departments_id` int NOT NULL,
  `course_choose` smallint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_courses`
--

INSERT INTO `api_courses` (`course`, `course_name`, `course_credits`, `course_departments_id`, `course_choose`) VALUES
(5, '网络基础', 2, 1007, 2),
(6, 'python程序设计', 2, 1007, 2),
(9, '中华诗词之美', 3, 1007, 1),
(12, 'OpenStack与虚拟化', 3, 1007, 2),
(13, 'web后端技术开发与应用', 2, 1007, 1),
(14, '数据结构', 3, 1007, 2),
(15, '选修2', 2, 1027, 1),
(16, '选修3', 2, 1027, 1);

-- --------------------------------------------------------

--
-- 表的结构 `api_course_selection`
--

CREATE TABLE `api_course_selection` (
  `id` bigint NOT NULL,
  `course` smallint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_course_selection`
--

INSERT INTO `api_course_selection` (`id`, `course`) VALUES
(1, 1);

-- --------------------------------------------------------

--
-- 表的结构 `api_departments`
--

CREATE TABLE `api_departments` (
  `departments` int NOT NULL,
  `departments_name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_departments`
--

INSERT INTO `api_departments` (`departments`, `departments_name`) VALUES
(1007, '计算机信息学院'),
(1024, '测绘学院'),
(1027, '马克思主义学院'),
(1028, '冶金与矿业学院'),
(1029, '电气与机械学院'),
(1030, '建筑工程学院'),
(1031, '环境与化工学院'),
(1032, '商学院'),
(1033, '外语学院'),
(1034, '艺术设计学院'),
(1035, '继续教育与培训学院'),
(1036, '通识与素质教育学院');

-- --------------------------------------------------------

--
-- 表的结构 `api_electives`
--

CREATE TABLE `api_electives` (
  `electives` int NOT NULL,
  `course_results` int NOT NULL,
  `course_id` int NOT NULL,
  `student_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_electives`
--

INSERT INTO `api_electives` (`electives`, `course_results`, `course_id`, `student_id`) VALUES
(1, 1, 6, 1007080601),
(2, 2, 6, 1007080602),
(5, 2, 5, 1007080601),
(6, 0, 5, 1007080602),
(7, 0, 5, 1007080603),
(8, 0, 5, 1007080604),
(9, 0, 5, 1007080605),
(10, 0, 12, 1007080601),
(11, 0, 12, 1007080602),
(12, 0, 12, 1007080603),
(13, 0, 12, 1007080604),
(14, 0, 12, 1007080605),
(15, 0, 13, 1007080601),
(16, 0, 13, 1007080602),
(17, 0, 13, 1007080603),
(18, 0, 13, 1007080604),
(19, 0, 13, 1007080605),
(20, 0, 14, 1007080601),
(21, 0, 14, 1007080602),
(22, 0, 14, 1007080603),
(23, 0, 14, 1007080604),
(24, 0, 14, 1007080605);

-- --------------------------------------------------------

--
-- 表的结构 `api_professional`
--

CREATE TABLE `api_professional` (
  `professional` int NOT NULL,
  `professional_name` varchar(255) NOT NULL,
  `administrator_departments_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_professional`
--

INSERT INTO `api_professional` (`professional`, `professional_name`, `administrator_departments_id`) VALUES
(8, '计算机网络技术', 1007),
(12, '现代通信技术', 1007),
(13, '物联网应用技术', 1007),
(14, '人工智能技术应用', 1007),
(15, '信息安全技术应用', 1007),
(16, '大数据技术', 1007);

-- --------------------------------------------------------

--
-- 表的结构 `api_root`
--

CREATE TABLE `api_root` (
  `id` int NOT NULL,
  `password` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_root`
--

INSERT INTO `api_root` (`id`, `password`) VALUES
(8888, '3a6c7f9e30e0b3737ce7e0a8b0a8107c');

-- --------------------------------------------------------

--
-- 表的结构 `api_students`
--

CREATE TABLE `api_students` (
  `student` int NOT NULL,
  `student_name` varchar(32) NOT NULL,
  `student_gender` smallint NOT NULL,
  `student_time` date NOT NULL,
  `student_class_id` int NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `mail` varchar(254) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_students`
--

INSERT INTO `api_students` (`student`, `student_name`, `student_gender`, `student_time`, `student_class_id`, `password`, `mail`) VALUES
(1007080601, 'fhy', 1, '2022-12-02', 6, '67fdbb10295e3182e4a859399e283e19', 'zhao2073981548@163.com'),
(1007080602, 'zzz', 1, '2022-11-30', 6, 'd852f5a6ef0ded15616e1d81ab0b807e', 'zhao2073981548@163.com'),
(1007080603, '张伟', 1, '2000-02-09', 6, '3a5579c1afb0a75c0c61280394c3c514', 'zhao2073981548@163.com'),
(1007080604, '张三', 1, '2022-12-08', 6, '00e3548519289dab85458cb9534946a3', 'zhao2073981548@163.com'),
(1007080605, '李四', 1, '2022-12-08', 6, '62472635b9c73242bb6bf1fd4e514a73', 'zhao2073981548@163.com');

-- --------------------------------------------------------

--
-- 表的结构 `api_teacher`
--

CREATE TABLE `api_teacher` (
  `teacher` int NOT NULL,
  `teacher_name` varchar(64) NOT NULL,
  `teacher_gender` smallint NOT NULL,
  `teacher_time` date NOT NULL,
  `teacher_phone` int NOT NULL,
  `teacher_departments_id` int NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `mail` varchar(254) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_teacher`
--

INSERT INTO `api_teacher` (`teacher`, `teacher_name`, `teacher_gender`, `teacher_time`, `teacher_phone`, `teacher_departments_id`, `password`, `mail`) VALUES
(1007001, '王老师', 1, '2022-10-20', 153153153, 1007, '76cc0e72061e69a24078712255a7c670', 'zhao2073981548@163.com'),
(1007002, '李老师', 1, '2015-06-17', 1234560101, 1007, '76cc0e72061e69a24078712255a7c670', 'zhao2073981548@163.com'),
(1007003, '胡老师', 1, '1996-07-11', 123456789, 1007, '76cc0e72061e69a24078712255a7c670', 'zhao2073981548@163.com'),
(1024001, '赵老师', 1, '2020-06-17', 12, 1024, '76cc0e72061e69a24078712255a7c670', 'zhao2073981548@163.com'),
(1024002, '张老师', 1, '2022-12-02', 123456789, 1024, '76cc0e72061e69a24078712255a7c670', 'admin@kmyzsec.net');

-- --------------------------------------------------------

--
-- 表的结构 `api_teaching`
--

CREATE TABLE `api_teaching` (
  `id` bigint NOT NULL,
  `course_id` int NOT NULL,
  `teacher_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `api_teaching`
--

INSERT INTO `api_teaching` (`id`, `course_id`, `teacher_id`) VALUES
(3, 5, 1024001),
(16, 5, 1007001),
(17, 6, 1024001),
(19, 6, 1007001),
(20, 14, 1007001);

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add administrator', 7, 'add_administrator'),
(26, 'Can change administrator', 7, 'change_administrator'),
(27, 'Can delete administrator', 7, 'delete_administrator'),
(28, 'Can view administrator', 7, 'view_administrator'),
(29, 'Can add class', 8, 'add_class'),
(30, 'Can change class', 8, 'change_class'),
(31, 'Can delete class', 8, 'delete_class'),
(32, 'Can view class', 8, 'view_class'),
(33, 'Can add courses', 9, 'add_courses'),
(34, 'Can change courses', 9, 'change_courses'),
(35, 'Can delete courses', 9, 'delete_courses'),
(36, 'Can view courses', 9, 'view_courses'),
(37, 'Can add departments', 10, 'add_departments'),
(38, 'Can change departments', 10, 'change_departments'),
(39, 'Can delete departments', 10, 'delete_departments'),
(40, 'Can view departments', 10, 'view_departments'),
(41, 'Can add root', 11, 'add_root'),
(42, 'Can change root', 11, 'change_root'),
(43, 'Can delete root', 11, 'delete_root'),
(44, 'Can view root', 11, 'view_root'),
(45, 'Can add students', 12, 'add_students'),
(46, 'Can change students', 12, 'change_students'),
(47, 'Can delete students', 12, 'delete_students'),
(48, 'Can view students', 12, 'view_students'),
(49, 'Can add teacher', 13, 'add_teacher'),
(50, 'Can change teacher', 13, 'change_teacher'),
(51, 'Can delete teacher', 13, 'delete_teacher'),
(52, 'Can view teacher', 13, 'view_teacher'),
(53, 'Can add administrator_ login', 14, 'add_administrator_login'),
(54, 'Can change administrator_ login', 14, 'change_administrator_login'),
(55, 'Can delete administrator_ login', 14, 'delete_administrator_login'),
(56, 'Can view administrator_ login', 14, 'view_administrator_login'),
(57, 'Can add students_ login', 15, 'add_students_login'),
(58, 'Can change students_ login', 15, 'change_students_login'),
(59, 'Can delete students_ login', 15, 'delete_students_login'),
(60, 'Can view students_ login', 15, 'view_students_login'),
(61, 'Can add teacher_ login', 16, 'add_teacher_login'),
(62, 'Can change teacher_ login', 16, 'change_teacher_login'),
(63, 'Can delete teacher_ login', 16, 'delete_teacher_login'),
(64, 'Can view teacher_ login', 16, 'view_teacher_login'),
(65, 'Can add professional', 17, 'add_professional'),
(66, 'Can change professional', 17, 'change_professional'),
(67, 'Can delete professional', 17, 'delete_professional'),
(68, 'Can view professional', 17, 'view_professional'),
(69, 'Can add electives', 18, 'add_electives'),
(70, 'Can change electives', 18, 'change_electives'),
(71, 'Can delete electives', 18, 'delete_electives'),
(72, 'Can view electives', 18, 'view_electives'),
(73, 'Can add teaching', 19, 'add_teaching'),
(74, 'Can change teaching', 19, 'change_teaching'),
(75, 'Can delete teaching', 19, 'delete_teaching'),
(76, 'Can view teaching', 19, 'view_teaching'),
(77, 'Can add class_course', 20, 'add_class_course'),
(78, 'Can change class_course', 20, 'change_class_course'),
(79, 'Can delete class_course', 20, 'delete_class_course'),
(80, 'Can view class_course', 20, 'view_class_course'),
(81, 'Can add course_selection', 21, 'add_course_selection'),
(82, 'Can change course_selection', 21, 'change_course_selection'),
(83, 'Can delete course_selection', 21, 'delete_course_selection'),
(84, 'Can view course_selection', 21, 'view_course_selection');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(7, 'api', 'administrator'),
(14, 'api', 'administrator_login'),
(8, 'api', 'class'),
(20, 'api', 'class_course'),
(21, 'api', 'course_selection'),
(9, 'api', 'courses'),
(10, 'api', 'departments'),
(18, 'api', 'electives'),
(17, 'api', 'professional'),
(11, 'api', 'root'),
(12, 'api', 'students'),
(15, 'api', 'students_login'),
(13, 'api', 'teacher'),
(16, 'api', 'teacher_login'),
(19, 'api', 'teaching'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-11-30 06:16:53.811074'),
(2, 'auth', '0001_initial', '2022-11-30 06:16:53.991437'),
(3, 'admin', '0001_initial', '2022-11-30 06:16:54.042661'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-11-30 06:16:54.048951'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-30 06:16:54.055137'),
(6, 'api', '0001_initial', '2022-11-30 06:16:54.330548'),
(7, 'contenttypes', '0002_remove_content_type_name', '2022-11-30 06:16:54.369485'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-11-30 06:16:54.393433'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-11-30 06:16:54.409105'),
(10, 'auth', '0004_alter_user_username_opts', '2022-11-30 06:16:54.416678'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-11-30 06:16:54.440176'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-11-30 06:16:54.442917'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-11-30 06:16:54.448954'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-11-30 06:16:54.476480'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-11-30 06:16:54.502816'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-11-30 06:16:54.517634'),
(17, 'auth', '0011_update_proxy_permissions', '2022-11-30 06:16:54.528914'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-11-30 06:16:54.559540'),
(19, 'sessions', '0001_initial', '2022-11-30 06:16:54.576731'),
(20, 'api', '0002_alter_students_student', '2022-11-30 08:20:42.799569'),
(21, 'api', '0003_teaching', '2022-11-30 09:51:17.560585'),
(22, 'api', '0004_remove_students_login_student_and_more', '2022-12-01 12:32:19.442840'),
(23, 'api', '0005_administrator_mail_students_mail_teacher_mail', '2022-12-04 04:56:21.607212'),
(24, 'api', '0006_alter_teacher_teacher', '2022-12-05 06:31:22.554518'),
(25, 'api', '0007_rename_teacher_teacher_teacherid', '2022-12-05 06:43:22.952165'),
(26, 'api', '0008_rename_teacherid_teacher_teacher', '2022-12-05 06:46:39.842546'),
(27, 'api', '0009_alter_teaching_course_alter_teaching_teacher_and_more', '2022-12-07 11:35:14.450045'),
(28, 'api', '0010_alter_teaching_course_alter_teaching_teacher', '2022-12-07 11:42:52.875917'),
(29, 'api', '0011_alter_teaching_unique_together', '2022-12-08 03:20:52.380904'),
(30, 'api', '0012_class_course', '2022-12-08 05:39:38.661634'),
(31, 'api', '0013_courses_course_choose', '2022-12-10 03:45:58.280845'),
(32, 'api', '0014_course_selection', '2022-12-10 10:39:09.736000'),
(33, 'api', '0015_remove_course_selection_course_and_more', '2022-12-10 10:44:36.398441');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0dsuz1x2oa8yqnyrnkxy4ujy2gsmikuv', 'N2YxZWI0Yzg1NzI5ZGFmNzhhYzIzZWQwYWQ0YTUwMDU4NGY3ZGViYzp7ImltYWdlX2NvZGUiOiIydzl0IiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MCwiaW5mbyI6eyJpZCI6MTAwNzAwMSwibmFtZSI6Ilx1NzM4Ylx1ODAwMVx1NWUwOCJ9fQ==', '2022-12-14 13:57:13.065993'),
('17pp6dcgejoqukh7a6kafldpwgmo468k', 'eyJpbWFnZV9jb2RlIjoiVTc2dCIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3YlD:bxiDhefWnSEZVRz6F9hwxsL3eq0_DAjAn8_ZgLVW1rU', '2022-12-09 08:30:35.748458'),
('25edg54t7sju65tffovq3bd25xh24i2h', 'ZjQ0Y2YzOTRmZWMxMTdmNTFkNzA5ZjY1Zjc2NzRhNDgwZGVmYjc3Yjp7ImltYWdlX2NvZGUiOiJWT3gyIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 03:53:10.143581'),
('29phqbmabsvhjm4nm9qtr748i3mjnwhq', 'eyJpbWFnZV9jb2RlIjoiYU5wWCIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p4cv3:bbMGMNzy_QP9BdwsK1LsA-smxYt0qwR1IRY_f6ldFyE', '2022-12-12 07:09:09.504487'),
('4a61x9ld0inbuoidk2kpmcpvj9864ifm', 'eyJpbWFnZV9jb2RlIjoiNTlqZyIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p583I:ePrOr9vUJTWTB6v5j4e_2s9HY8aVdz0AYsssKxjzcOM', '2022-12-13 16:23:44.577731'),
('51isabo1a466albek9f0951ckielhe7u', 'eyJpbWFnZV9jb2RlIjoiaHU3ZSIsIl9zZXNzaW9uX2V4cGlyeSI6NjAsImluZm8iOnsiaWQiOjEwMDcwMDEsIm5hbWUiOiJcdTczOGJcdTgwMDFcdTVlMDgifX0:1p3tpb:kFG0CnqWNFuLPqNmI6k7c2IMnnsjQhVr17QlxTzmKf4', '2022-12-10 07:00:31.938840'),
('5pjhb3isuyhmb9win5ctrwsui368wsh0', 'eyJpbWFnZV9jb2RlIjoiVlhtZyIsIl9zZXNzaW9uX2V4cGlyeSI6NjAsImluZm8iOnsiaWQiOjEwMDcwODA2MDEsIm5hbWUiOiJmaHkifX0:1p3YR1:BGuuwb90kE5oegvHF9Q03SHvurd6sHgR-aZakCEoF9U', '2022-12-09 08:09:43.021706'),
('65raj667j12m0ust8s3doqxblesjla6k', 'NDYxZWFhN2I0OGE1NGVhZmE4YTc3ODYxNDQyYWQ0MmU4MzY1YWU1Zjp7ImltYWdlX2NvZGUiOiJ2VFYxIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 07:52:55.418417'),
('68ay2zzqine5rti5pjlg2x4lyuhf9mhx', 'eyJpbWFnZV9jb2RlIjoiZmdzMyIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3VcM:URRB5SjWJ1J9fSh8aGi9GMKR35W1nJULNo6chUSH1GQ', '2022-12-09 05:09:14.847391'),
('6qn4wz3elg0sw1wvyrjtfumgnp9bs07s', 'MmU2NjE3ZjQwZmQyZWM1Yjk3YmFmYTA1Y2YxMDIzYjQwZTM5NGVjMjp7ImltYWdlX2NvZGUiOiJPTFVDIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 07:52:28.473793'),
('7bjx886ektu8myq3sbb5ocyw2e0lvxcv', 'eyJpbWFnZV9jb2RlIjoiczdjYiIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3VR2:WXNym_2iZcwpHEVXuUPyn7bWX_49JPBsf3-hKZEvT0E', '2022-12-09 04:57:32.390375'),
('7rrqxj13i9mmf8o84y7ik2pyk1gca0r9', 'NjA5N2Q3ZjM4NDk2ODlmNmY0NWY0YWMyM2M1MjY5N2I0NzRkNGNiMzp7ImltYWdlX2NvZGUiOiJrc01OIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 04:13:01.425247'),
('8sep3xpz5giic9uuqerv11sez94i2yhh', 'ZjFhZTExNzIzNzYzNDcyY2ExODcwNmIwYTExMDEwZGI5YTQ4MDUwOTp7ImltYWdlX2NvZGUiOiIxaWdTIiwiX3Nlc3Npb25fZXhwaXJ5IjoxNzI4MDAsImluZm8iOnsiaWQiOjEwMDcwLCJuYW1lIjoiXHU4YmExXHU3Yjk3XHU2NzNhIn19', '2022-12-22 03:48:37.736932'),
('985be4dsli5bfznujphl8qc8yopmgm6t', 'eyJpbWFnZV9jb2RlIjoiRFRGcyIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3rXk:JaxKFF-O6P3MdE_4LW_CqPRbQoQQNA50yCj0VDOH41A', '2022-12-10 04:33:56.981512'),
('9d0qeppn6wd1cc40j1a4av8ex98qyu8h', 'eyJpbWFnZV9jb2RlIjoiU1BRQiIsIl9zZXNzaW9uX2V4cGlyeSI6MTcyODAwLCJpbmZvIjp7ImlkIjo4ODg4fX0:1p4G1F:IaWp4u15MoaMJAtR1jmlv46qwRKFKJ03VQgvW7Apsj4', '2022-12-13 06:41:01.346779'),
('adtt58gz92lcs5cirmd0wg8jeranf7yu', 'eyJpbWFnZV9jb2RlIjoid0tTZSIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3YTp:RkBWmHcjKQoNd7_D0O12hKMN387783oIFT6m-dNrv0c', '2022-12-09 08:12:37.770193'),
('anjf5gekp6n4mp5umej2t3gkyk0pdznk', 'YzU2YjM2ZTk0YTM2YTU3ZDFkNzg2NGU0NjU5ZjE4N2ZmYzJjY2VmZDp7ImltYWdlX2NvZGUiOiJudktGIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-15 02:25:24.455541'),
('b2uld22tizq9r354xwo2x7827un807d6', 'M2IzNTlhMjI4Y2M1NDI1N2I1Y2YyOGRiMGRiYmNiMmE0N2FlMjIyZjp7ImltYWdlX2NvZGUiOiJPSkVJIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 03:22:16.996758'),
('c96gr41jybx09xu4ppme53bmgyrtmczd', 'ZGUwOTE1YzM0NGE2YjA5ODI1Yzc5ZGNkZDE1MWFhMjE3NjEyZjRjNTp7ImltYWdlX2NvZGUiOiJpSVhNIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 12:08:34.262586'),
('d9567ftmhxbwesx8x6yde6bfijddwt81', 'MDRmMTAzYjJjNjRjMzY2OGM2NjcyYThkMGI4ZDhmZWZmMmYwMGY4Mzp7ImltYWdlX2NvZGUiOiJCeHdyIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MCwiaW5mbyI6eyJpZCI6MTAwNzAsIm5hbWUiOiJcdThiYTFcdTdiOTdcdTY3M2EifX0=', '2022-12-14 07:34:54.688527'),
('el1h6s56idefkfdlyp5xbq6ibk3qjjat', 'eyJpbWFnZV9jb2RlIjoidTRURyIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p588m:HeOEVC5S-c8gEelvINAabv03h2f7iROMAr8fhP3niIM', '2022-12-13 16:29:24.185212'),
('fa4uvgsygs3yew6q4aiw9ua22vvk41y2', 'eyJpbWFnZV9jb2RlIjoiaHd0UyIsIl9zZXNzaW9uX2V4cGlyeSI6NjAsImluZm8iOnsiaWQiOjEwMjQxMTExMDEsIm5hbWUiOiJcdTVmMjBcdTRlMDkifX0:1p3rQZ:Q1P1i3i-V-CcV7Q6bIPOTHNf3uP8FZkvhKC7WTKwqBQ', '2022-12-10 04:26:31.900404'),
('fz5bch9hi9sna4p7fl1heb8hqmpj6xuk', 'eyJpbWFnZV9jb2RlIjoiNXBCaCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAsImluZm8iOnsiaWQiOjg4ODh9fQ:1p3xgq:ueZeCl-QIy489flXh10KIJvlfOyZWEiPUoPPS-86WDs', '2022-12-10 11:07:44.323918'),
('g296e5oy4s95glcxcyrj0qkzzwvdnwhq', 'eyJpbWFnZV9jb2RlIjoiYnB0ZyIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p56Al:eHin0nV5vN3JowxKTpP1_H4H0GK3mmMatRUrxs3A_rY', '2022-12-13 14:23:19.768585'),
('gigtm64arnfkfpmk14xm0gl6n7biv5lb', 'Yzc1NWFmZWU2Yzg2MWQ0NGIwN2I3ZGNkYTQ0NmYzNTgwZTcyOTc0ODp7ImltYWdlX2NvZGUiOiJNRlRxIiwiX3Nlc3Npb25fZXhwaXJ5IjoxNzI4MDAsImluZm8iOnsiaWQiOjEwMDcwLCJuYW1lIjoiXHU4YmExXHU3Yjk3XHU2NzNhIn19', '2022-12-16 13:30:28.391661'),
('h9z238374apn1ilos5y2998w0e1riicx', 'YmM3ZjJhNGFlZmE2OTIyYThkNTE4ZDMwMzY4Njc5MTc4YWE4ZmZmMjp7ImltYWdlX2NvZGUiOiJ6MXFsIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 12:06:59.733850'),
('hq8i7aaljur77o0x6neq1a1saenkm7e8', 'ZTQ2MDNlYmEzNjIzMmMwNGZiMjM5MDViYmFkOTJjODNlMWUwZTBhYzp7ImltYWdlX2NvZGUiOiJFejUzIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MCwiaW5mbyI6eyJpZCI6MTAwNzA4MDYwMiwibmFtZSI6Inp6eiJ9fQ==', '2022-12-14 05:24:21.411590'),
('imnn13q25ib0y4k9opa4idcj05g0u8ym', 'MmRlODRhYjkwNGI2ZWVjMjVlMzczYTE5Yzc4YmY5MzhiMGM4YjIzOTp7ImltYWdlX2NvZGUiOiJIU3AwIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 13:57:54.541228'),
('isbtwjz6outwc4e5i93h7q0sdwjvpnti', 'eyJpbWFnZV9jb2RlIjoiblFEcyIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3BFL:Drfjw7YOb0GEpAZH5JlmgiA7Q51-brqs_zdYa6GQohU', '2022-12-08 07:24:07.731072'),
('k20g9zdh98zuqvoiy74zz8w165a1txcv', 'eyJpbWFnZV9jb2RlIjoiUGpDYyIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3Zdd:jX0EUDMXKPNOH9WSKQqaHD0tUy_mIQGy-9hB3BuHzbY', '2022-12-09 09:26:49.590160'),
('ktf76rq7srbvw24tcp1ju7950u837f2b', 'eyJpbWFnZV9jb2RlIjoiVHE4UCIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p4cvE:Ncf4vPV6miQzyvUgi69Y16YvfA3oj4pwneEZJ-WyJwM', '2022-12-12 07:09:20.378712'),
('ktpmeti99cwe5w061k1io7ikgxqi9w2y', 'eyJpbWFnZV9jb2RlIjoiNUUzViIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p57qf:YQJLBYCTP-YmJGewcROz843hTPTpeCkIQel82mePsZA', '2022-12-13 16:10:41.189323'),
('laumn1ororusmbuhddl9mf4dzh1doluk', 'ZjBhNTYwYmQxNjJiZDE2YzYyMjZiMGE0NTlhODViZjMxZjIwNzk0Mjp7ImltYWdlX2NvZGUiOiJwN255IiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-19 10:14:01.254357'),
('pfn5bc93krsf78cd1acn6z3vsbs8eorl', 'YWNlODE3NDNjMGQzZDE1OWFkNjNiNDg1ODA5OGY3ZjgzODIxYTkwYzp7ImltYWdlX2NvZGUiOiJBdUQ3IiwiX3Nlc3Npb25fZXhwaXJ5IjoxNzI4MDAsImluZm8iOnsiaWQiOjEwMDcwLCJuYW1lIjoiXHU4YmExXHU3Yjk3XHU2NzNhIn19', '2022-12-15 17:00:08.298852'),
('pun8yog1uobiaxhmlgvonc2s4a1yrid3', 'ODU5NWFiOWNiYzBiMDI1YjJjNmM3OThmN2FkMjQ0ODZkOTZmODA3MTp7ImltYWdlX2NvZGUiOiIwU2RNIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MCwiaW5mbyI6eyJpZCI6MTAwNzAsIm5hbWUiOiJcdThiYTFcdTdiOTdcdTY3M2EifX0=', '2022-12-20 03:49:18.547668'),
('qrcnqvpk1x7n1ab372aw048luq9e1x8y', 'eyJpbWFnZV9jb2RlIjoiS0Q4dSIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p3t4x:7zhq0qrYXegwlUfuGtV6raHApm685RFpTTx0Yy5Fpkw', '2022-12-10 06:12:19.495895'),
('qtpi7f9lb13ph65qjno1lnkywaqqfigy', 'ODBlNzkzOWYzYmU2YzkyYWU0ZTNmNGI1YTg3NmU1YmU2ZTc4NmZlMTp7ImltYWdlX2NvZGUiOiIxQ3FCIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-13 17:19:27.194339'),
('t27iajkh98kj1mn2r8yehe1ytnud2kh3', 'eyJpbWFnZV9jb2RlIjoiOGV0aiIsIl9zZXNzaW9uX2V4cGlyeSI6NjB9:1p4YoR:6RATh4rlJYsevQaI4XsaO1UA7IUBsGqlfYo0GkZjuZw', '2022-12-12 02:46:03.208822'),
('t6bxqx4bwlbhssw8zr29hzj6g6unspu9', 'eyJpbWFnZV9jb2RlIjoiWHlXeCIsIl9zZXNzaW9uX2V4cGlyeSI6NjAsImluZm8iOnsiaWQiOjEwMjQxMTExMDEsIm5hbWUiOiJcdTVmMjBcdTRlMDkifX0:1p4YYc:N54R-5nYnQUzFDJpVO60eSiQU2PeD2Lxpic8y__lyFw', '2022-12-12 02:29:42.890734'),
('tk1wq5wr38i8vjb4gh3rv85s977ghp09', 'ZjA4ZGQxNTVkZWNmMWY4M2VhMTRhOWZmNWQ1N2U0ODdjYmFjYzY1Yzp7ImltYWdlX2NvZGUiOiJ1Mm9VIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-15 01:40:59.373342'),
('v0jj74wivqe766ei9o0tj08nyyvqoia0', 'YzY3YzhmN2NjNjgyMmM2NWIxZWM2Y2ZhODRmNTZkYzU3Y2I5OTk2ZDp7ImltYWdlX2NvZGUiOiJwdUI3IiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MCwiaW5mbyI6eyJpZCI6MTAwNzAsIm5hbWUiOiJcdThiYTFcdTdiOTdcdTY3M2EifX0=', '2022-12-13 17:13:19.883978'),
('vk8es193qz5pu2f96bmszrinafzelo60', 'OTJjOTNlZGUxNWZmOGVlOGYxOGRjMWJkZGRiYjViNTMyMDhmY2Y4Yzp7ImltYWdlX2NvZGUiOiJuZ29OIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-15 02:03:07.296995'),
('yw5inuijq0a8usbew5hybtwoawinzaz2', 'OGVkNTYyNTZlZDQxNTQ5MzRiYWE2YjI0ZWM5NTVmOGQ3ZjkwNWEwYTp7ImltYWdlX2NvZGUiOiJoR0tmIiwiX3Nlc3Npb25fZXhwaXJ5IjoxNzI4MDAsImluZm8iOnsiaWQiOjEwMDcwODA2MDIsIm5hbWUiOiJ6enoifX0=', '2022-12-18 03:37:18.352309'),
('zj1u70szyn41cn05fpu4tdoh0pihiboc', 'NDc4NjZkMGQ5OTBiZjEwZjY4NzAzMGRjMzU0MzYxNzQyNDY1YTNjYTp7ImltYWdlX2NvZGUiOiI0aXdYIiwiX3Nlc3Npb25fZXhwaXJ5Ijo2MH0=', '2022-12-14 13:11:43.133194');

--
-- 转储表的索引
--

--
-- 表的索引 `api_administrator`
--
ALTER TABLE `api_administrator`
  ADD PRIMARY KEY (`administrator`),
  ADD KEY `api_administrator_administrator_depart_5b12b9af_fk_api_depar` (`administrator_departments_id`);

--
-- 表的索引 `api_class`
--
ALTER TABLE `api_class`
  ADD PRIMARY KEY (`classID`),
  ADD KEY `api_class_professional_id_d51858ad_fk_api_profe` (`professional_id`);

--
-- 表的索引 `api_class_course`
--
ALTER TABLE `api_class_course`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_class_course_classid_id_fc81117e_fk_api_class_classID` (`classid_id`),
  ADD KEY `api_class_course_course_id_aaf1c8ba_fk_api_courses_course` (`course_id`);

--
-- 表的索引 `api_courses`
--
ALTER TABLE `api_courses`
  ADD PRIMARY KEY (`course`),
  ADD KEY `api_courses_course_departments_i_c1d5ae53_fk_api_depar` (`course_departments_id`);

--
-- 表的索引 `api_course_selection`
--
ALTER TABLE `api_course_selection`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `api_departments`
--
ALTER TABLE `api_departments`
  ADD PRIMARY KEY (`departments`);

--
-- 表的索引 `api_electives`
--
ALTER TABLE `api_electives`
  ADD PRIMARY KEY (`electives`),
  ADD KEY `api_electives_course_id_644bcf4c_fk_api_courses_course` (`course_id`),
  ADD KEY `api_electives_student_id_6f380f93_fk` (`student_id`);

--
-- 表的索引 `api_professional`
--
ALTER TABLE `api_professional`
  ADD PRIMARY KEY (`professional`),
  ADD KEY `api_professional_administrator_depart_a08c8dd9_fk_api_depar` (`administrator_departments_id`);

--
-- 表的索引 `api_root`
--
ALTER TABLE `api_root`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `api_students`
--
ALTER TABLE `api_students`
  ADD PRIMARY KEY (`student`),
  ADD KEY `api_students_student_class_id_83a70aff_fk_api_class_classID` (`student_class_id`);

--
-- 表的索引 `api_teacher`
--
ALTER TABLE `api_teacher`
  ADD PRIMARY KEY (`teacher`),
  ADD KEY `api_teacher_teacher_departments__35ca4427_fk_api_depar` (`teacher_departments_id`);

--
-- 表的索引 `api_teaching`
--
ALTER TABLE `api_teaching`
  ADD PRIMARY KEY (`id`),
  ADD KEY `api_teaching_course_id_e8f7f662_fk` (`course_id`),
  ADD KEY `api_teaching_teacher_id_db9266ca` (`teacher_id`);

--
-- 表的索引 `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 表的索引 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- 表的索引 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- 表的索引 `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- 表的索引 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- 表的索引 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- 表的索引 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- 表的索引 `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- 表的索引 `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `api_administrator`
--
ALTER TABLE `api_administrator`
  MODIFY `administrator` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10251;

--
-- 使用表AUTO_INCREMENT `api_class`
--
ALTER TABLE `api_class`
  MODIFY `classID` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- 使用表AUTO_INCREMENT `api_class_course`
--
ALTER TABLE `api_class_course`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- 使用表AUTO_INCREMENT `api_courses`
--
ALTER TABLE `api_courses`
  MODIFY `course` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- 使用表AUTO_INCREMENT `api_course_selection`
--
ALTER TABLE `api_course_selection`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用表AUTO_INCREMENT `api_departments`
--
ALTER TABLE `api_departments`
  MODIFY `departments` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1037;

--
-- 使用表AUTO_INCREMENT `api_electives`
--
ALTER TABLE `api_electives`
  MODIFY `electives` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- 使用表AUTO_INCREMENT `api_professional`
--
ALTER TABLE `api_professional`
  MODIFY `professional` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- 使用表AUTO_INCREMENT `api_root`
--
ALTER TABLE `api_root`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8889;

--
-- 使用表AUTO_INCREMENT `api_teaching`
--
ALTER TABLE `api_teaching`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- 使用表AUTO_INCREMENT `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=85;

--
-- 使用表AUTO_INCREMENT `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- 使用表AUTO_INCREMENT `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- 限制导出的表
--

--
-- 限制表 `api_administrator`
--
ALTER TABLE `api_administrator`
  ADD CONSTRAINT `api_administrator_administrator_depart_5b12b9af_fk_api_depar` FOREIGN KEY (`administrator_departments_id`) REFERENCES `api_departments` (`departments`);

--
-- 限制表 `api_class`
--
ALTER TABLE `api_class`
  ADD CONSTRAINT `api_class_professional_id_d51858ad_fk_api_profe` FOREIGN KEY (`professional_id`) REFERENCES `api_professional` (`professional`);

--
-- 限制表 `api_class_course`
--
ALTER TABLE `api_class_course`
  ADD CONSTRAINT `api_class_course_classid_id_fc81117e_fk_api_class_classID` FOREIGN KEY (`classid_id`) REFERENCES `api_class` (`classID`),
  ADD CONSTRAINT `api_class_course_course_id_aaf1c8ba_fk_api_courses_course` FOREIGN KEY (`course_id`) REFERENCES `api_courses` (`course`);

--
-- 限制表 `api_courses`
--
ALTER TABLE `api_courses`
  ADD CONSTRAINT `api_courses_course_departments_i_c1d5ae53_fk_api_depar` FOREIGN KEY (`course_departments_id`) REFERENCES `api_departments` (`departments`);

--
-- 限制表 `api_electives`
--
ALTER TABLE `api_electives`
  ADD CONSTRAINT `api_electives_course_id_644bcf4c_fk_api_courses_course` FOREIGN KEY (`course_id`) REFERENCES `api_courses` (`course`),
  ADD CONSTRAINT `api_electives_student_id_6f380f93_fk` FOREIGN KEY (`student_id`) REFERENCES `api_students` (`student`);

--
-- 限制表 `api_professional`
--
ALTER TABLE `api_professional`
  ADD CONSTRAINT `api_professional_administrator_depart_a08c8dd9_fk_api_depar` FOREIGN KEY (`administrator_departments_id`) REFERENCES `api_departments` (`departments`);

--
-- 限制表 `api_students`
--
ALTER TABLE `api_students`
  ADD CONSTRAINT `api_students_student_class_id_83a70aff_fk_api_class_classID` FOREIGN KEY (`student_class_id`) REFERENCES `api_class` (`classID`);

--
-- 限制表 `api_teacher`
--
ALTER TABLE `api_teacher`
  ADD CONSTRAINT `api_teacher_teacher_departments__35ca4427_fk_api_depar` FOREIGN KEY (`teacher_departments_id`) REFERENCES `api_departments` (`departments`);

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
