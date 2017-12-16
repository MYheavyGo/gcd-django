# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stddata', '0002_initial_data'),
        ('gcd', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Awards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gcd_official_name', models.CharField(max_length=255, db_index=True)),
                ('whos_who', models.URLField(null=True)),
                ('birth_country_uncertain', models.BooleanField(default=False)),
                ('birth_province', models.CharField(max_length=50)),
                ('birth_province_uncertain', models.BooleanField(default=False)),
                ('birth_city', models.CharField(max_length=200)),
                ('birth_city_uncertain', models.BooleanField(default=False)),
                ('death_country_uncertain', models.BooleanField(default=False)),
                ('death_province', models.CharField(max_length=50)),
                ('death_province_uncertain', models.BooleanField(default=False)),
                ('death_city', models.CharField(max_length=200)),
                ('death_city_uncertain', models.BooleanField(default=False)),
                ('bio', models.TextField()),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('birth_country', models.ForeignKey(related_name='birth_country', to='stddata.Country', null=True)),
                ('birth_date', models.ForeignKey(related_name='+', to='stddata.Date', null=True)),
            ],
            options={
                'ordering': ('gcd_official_name', 'created'),
                'verbose_name_plural': 'Creators',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorArtInfluence',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('influence_name', models.CharField(max_length=200)),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('creator', models.ForeignKey(related_name='art_influence_set', to='gcd.Creator')),
            ],
            options={
                'db_table': 'gcd_creator_art_influence',
                'verbose_name_plural': 'Creator Art Influences',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorAward',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('award_name', models.CharField(max_length=255)),
                ('no_award_name', models.BooleanField(default=False)),
                ('award_year', models.PositiveSmallIntegerField(null=True)),
                ('award_year_uncertain', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('award', models.ForeignKey(to='gcd.Award', null=True)),
                ('creator', models.ForeignKey(related_name='award_set', to='gcd.Creator')),
            ],
            options={
                'ordering': ('award_year',),
                'db_table': 'gcd_creator_award',
                'verbose_name_plural': 'Creator Awards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorDegree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree_year', models.PositiveSmallIntegerField(null=True)),
                ('degree_year_uncertain', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('creator', models.ForeignKey(related_name='degree_set', to='gcd.Creator')),
            ],
            options={
                'ordering': ('degree_year',),
                'db_table': 'gcd_creator_degree',
                'verbose_name_plural': 'Creator Degrees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorMembership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('organization_name', models.CharField(max_length=200)),
                ('membership_year_began', models.PositiveSmallIntegerField(null=True)),
                ('membership_year_began_uncertain', models.BooleanField(default=False)),
                ('membership_year_ended', models.PositiveSmallIntegerField(null=True)),
                ('membership_year_ended_uncertain', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('creator', models.ForeignKey(related_name='membership_set', to='gcd.Creator')),
            ],
            options={
                'ordering': ('membership_type',),
                'db_table': 'gcd_creator_membership',
                'verbose_name_plural': 'Creator Memberships',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorNameDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, db_index=True)),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('creator', models.ForeignKey(related_name='creator_names', to='gcd.Creator')),
            ],
            options={
                'ordering': ['type__id', 'created', '-id'],
                'db_table': 'gcd_creator_name_detail',
                'verbose_name_plural': 'CreatorName Details',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorNonComicWork',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publication_title', models.CharField(max_length=200)),
                ('employer_name', models.CharField(max_length=200)),
                ('work_title', models.CharField(max_length=255)),
                ('work_urls', models.TextField()),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('creator', models.ForeignKey(related_name='non_comic_work_set', to='gcd.Creator')),
            ],
            options={
                'ordering': ('publication_title', 'employer_name', 'work_type'),
                'db_table': 'gcd_creator_non_comic_work',
                'verbose_name_plural': 'Creator Non Comic Works',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'ordering': ('to_creator', 'relation_type', 'from_creator'),
                'db_table': 'gcd_creator_relation',
                'verbose_name_plural': 'Creator Relations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CreatorSchool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_year_began', models.PositiveSmallIntegerField(null=True)),
                ('school_year_began_uncertain', models.BooleanField(default=False)),
                ('school_year_ended', models.PositiveSmallIntegerField(null=True)),
                ('school_year_ended_uncertain', models.BooleanField(default=False)),
                ('notes', models.TextField()),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
                ('creator', models.ForeignKey(related_name='school_set', to='gcd.Creator')),
            ],
            options={
                'ordering': ('school_year_began', 'school_year_ended'),
                'db_table': 'gcd_creator_school',
                'verbose_name_plural': 'Creator Schools',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DataSource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('source_description', models.TextField()),
                ('field', models.CharField(max_length=256)),
                ('reserved', models.BooleanField(default=False, db_index=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'ordering': ('source_description',),
                'db_table': 'gcd_data_source',
                'verbose_name_plural': 'Creator Data Source',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('degree_name',),
                'verbose_name_plural': 'Degrees',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MembershipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'gcd_membership_type',
                'verbose_name_plural': 'Membership Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NameType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('type',),
                'db_table': 'gcd_name_type',
                'verbose_name_plural': 'Name Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NonComicWorkRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'gcd_non_comic_work_role',
                'verbose_name_plural': 'NonComic Work Roles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NonComicWorkType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'gcd_non_comic_work_type',
                'verbose_name_plural': 'NonComic Work Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NonComicWorkYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_year', models.PositiveSmallIntegerField(null=True)),
                ('work_year_uncertain', models.BooleanField(default=False)),
                ('non_comic_work', models.ForeignKey(related_name='noncomicworkyears', to='gcd.CreatorNonComicWork')),
            ],
            options={
                'ordering': ('work_year',),
                'db_table': 'gcd_non_comic_work_year',
                'verbose_name_plural': 'NonComic Work Years',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
                ('reverse_type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('type',),
                'db_table': 'gcd_relation_type',
                'verbose_name_plural': 'Relation Types',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school_name', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('school_name',),
                'verbose_name_plural': 'Schools',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ('type',),
                'db_table': 'gcd_source_type',
                'verbose_name_plural': 'Source Types',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='datasource',
            name='source_type',
            field=models.ForeignKey(to='gcd.SourceType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorschool',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorschool',
            name='school',
            field=models.ForeignKey(related_name='creator', to='gcd.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorrelation',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorrelation',
            name='from_creator',
            field=models.ForeignKey(related_name='to_related_creator', to='gcd.Creator'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorrelation',
            name='relation_type',
            field=models.ForeignKey(related_name='relation_type', to='gcd.RelationType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorrelation',
            name='to_creator',
            field=models.ForeignKey(related_name='from_related_creator', to='gcd.Creator'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatornoncomicwork',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatornoncomicwork',
            name='work_role',
            field=models.ForeignKey(to='gcd.NonComicWorkRole', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatornoncomicwork',
            name='work_type',
            field=models.ForeignKey(to='gcd.NonComicWorkType'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatornamedetail',
            name='type',
            field=models.ForeignKey(related_name='nametypes', to='gcd.NameType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatormembership',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatormembership',
            name='membership_type',
            field=models.ForeignKey(to='gcd.MembershipType', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatordegree',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatordegree',
            name='degree',
            field=models.ForeignKey(related_name='creator', to='gcd.Degree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatordegree',
            name='school',
            field=models.ForeignKey(related_name='degree', to='gcd.School', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatoraward',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorartinfluence',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creatorartinfluence',
            name='influence_link',
            field=models.ForeignKey(related_name='exist_influencer', to='gcd.Creator', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='data_source',
            field=models.ManyToManyField(to='gcd.DataSource'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='death_country',
            field=models.ForeignKey(related_name='death_country', to='stddata.Country', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='death_date',
            field=models.ForeignKey(related_name='+', to='stddata.Date', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='degrees',
            field=models.ManyToManyField(related_name='degreeinformation', null=True, through='gcd.CreatorDegree', to='gcd.Degree'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='creator',
            name='schools',
            field=models.ManyToManyField(related_name='schoolinformation', null=True, through='gcd.CreatorSchool', to='gcd.School'),
            preserve_default=True,
        ),
    ]