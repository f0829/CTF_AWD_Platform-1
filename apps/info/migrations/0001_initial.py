# Generated by Django 2.1.7 on 2019-05-03 19:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choice', '0001_initial'),
        ('ctf', '0001_initial'),
        ('competition', '0001_initial'),
        ('teams', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AwdSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('awd_submit_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('awd_submit_flag', models.CharField(max_length=255, verbose_name='提交flag')),
                ('awd_submit_result', models.BooleanField(verbose_name='判定结果')),
                ('awd_submit_teamid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_id', to='teams.TeamProfile', verbose_name='目标队伍编号')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_id', to='competition.CompetitionProfile', verbose_name='比赛')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamProfile', verbose_name='队伍')),
            ],
            options={
                'verbose_name': 'AWD提交flag',
                'verbose_name_plural': 'AWD提交flag',
            },
        ),
        migrations.CreateModel(
            name='ChoiceResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_result_result', models.SmallIntegerField(choices=[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D')], verbose_name='选择答案')),
            ],
            options={
                'verbose_name': '选择题选项',
                'verbose_name_plural': '选择题选项',
            },
        ),
        migrations.CreateModel(
            name='CompetitionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition_choice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choice_1', to='choice.ChoiceLibrary', verbose_name='选择题ID')),
                ('competition_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_1', to='competition.CompetitionProfile')),
            ],
            options={
                'verbose_name': '选择题抽取题目',
                'verbose_name_plural': '选择题抽取题目',
            },
        ),
        migrations.CreateModel(
            name='CtfCompetitionTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_times', models.IntegerField(default=0, verbose_name='正确提交次数')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.CompetitionProfile', verbose_name='比赛编号')),
                ('ctf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.CtfLibrary', verbose_name='题目编号')),
            ],
            options={
                'verbose_name': '比赛CTF题目',
                'verbose_name_plural': '比赛CTF题目',
            },
        ),
        migrations.CreateModel(
            name='CtfSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='提交时间')),
                ('submit_flag', models.CharField(max_length=255, verbose_name='提交flag')),
                ('submit_result', models.BooleanField(verbose_name='判定结果')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.CompetitionProfile', verbose_name='比赛')),
                ('submit_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ctf.CtfLibrary', verbose_name='提交题目')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamProfile', verbose_name='队伍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='队员')),
            ],
            options={
                'verbose_name': 'CTF提交flag',
                'verbose_name_plural': 'CTF提交flag',
            },
        ),
        migrations.CreateModel(
            name='Illegality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illegality_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='')),
                ('illegality_action', models.SmallIntegerField(choices=[(0, '作弊'), (1, '攻击平台'), (2, '其他')], default=2, verbose_name='行为')),
                ('illegality_timea', models.IntegerField(verbose_name='违规次数')),
                ('illegality_duration', models.IntegerField(verbose_name='封禁时间')),
                ('illegality_starttime', models.DateTimeField(verbose_name='封禁开始时间')),
                ('illegality_endtime', models.DateTimeField(verbose_name='封禁结束时间')),
                ('duration_status', models.BooleanField(verbose_name='封禁状态')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.CompetitionProfile', verbose_name='比赛')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamProfile', verbose_name='队伍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='队员')),
            ],
            options={
                'verbose_name': '比赛违规',
                'verbose_name_plural': '比赛违规',
            },
        ),
        migrations.CreateModel(
            name='TeamCompetitionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_all', models.IntegerField(default=0, verbose_name='队伍总得分')),
                ('score_choice', models.IntegerField(default=0, verbose_name='选择题得分')),
                ('score_ctf', models.IntegerField(default=0, verbose_name='ctf分数')),
                ('score_awd', models.IntegerField(default=0, verbose_name='awd分数')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.CompetitionProfile', verbose_name='比赛')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamProfile', verbose_name='队伍')),
            ],
            options={
                'verbose_name': '比赛情况',
                'verbose_name_plural': '比赛情况',
            },
        ),
        migrations.CreateModel(
            name='UserCompetitionInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_all', models.IntegerField(default=0, verbose_name='个人总分')),
                ('score_choice', models.IntegerField(default=0, verbose_name='选择题分数')),
                ('score_ctf', models.IntegerField(default=0, verbose_name='ctf总分')),
                ('score_awd', models.IntegerField(default=0, verbose_name='awd总分')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition.CompetitionProfile', verbose_name='比赛')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.TeamProfile', verbose_name='队伍')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='队员')),
            ],
            options={
                'verbose_name': '比赛情况',
                'verbose_name_plural': '比赛情况',
            },
        ),
        migrations.AddField(
            model_name='choiceresult',
            name='choice_result_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competition_choice_idd', to='info.CompetitionChoice', verbose_name='选择题ID'),
        ),
        migrations.AlterUniqueTogether(
            name='usercompetitioninfo',
            unique_together={('user', 'team', 'competition')},
        ),
        migrations.AlterUniqueTogether(
            name='teamcompetitioninfo',
            unique_together={('team', 'competition')},
        ),
        migrations.AlterUniqueTogether(
            name='illegality',
            unique_together={('user', 'team', 'competition')},
        ),
        migrations.AlterUniqueTogether(
            name='ctfcompetitiontable',
            unique_together={('ctf', 'competition')},
        ),
        migrations.AlterUniqueTogether(
            name='competitionchoice',
            unique_together={('competition_choice_id', 'competition_id')},
        ),
        migrations.AlterUniqueTogether(
            name='awdsubmit',
            unique_together={('team', 'competition')},
        ),
    ]
