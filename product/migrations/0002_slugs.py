import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models
from django.utils.text import slugify

def populate_slugs(apps, schema_editor):
    """Populate empty slug fields with unique values before adding unique constraint"""
    Category = apps.get_model('product', 'Category')
    Product = apps.get_model('product', 'Product')
    
    # Handle Category slugs
    try:
        categories = Category.objects.filter(slug__isnull=True) | Category.objects.filter(slug='')
        for i, category in enumerate(categories):
            base_slug = slugify(category.title) if category.title else f'category-{category.id}'
            slug = base_slug
            counter = 1
            
            # Ensure uniqueness
            while Category.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            
            category.slug = slug
            category.save()
    except Exception as e:
        print(f"Error populating category slugs: {e}")
    
    # Handle Product slugs
    try:
        products = Product.objects.filter(slug__isnull=True) | Product.objects.filter(slug='')
        for i, product in enumerate(products):
            base_slug = slugify(product.title) if product.title else f'product-{product.id}'
            slug = base_slug
            counter = 1
            
            # Ensure uniqueness
            while Product.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            
            product.slug = slug
            product.save()
    except Exception as e:
        print(f"Error populating product slugs: {e}")


def reverse_populate_slugs(apps, schema_editor):
    """Reverse migration - clear slugs"""
    try:
        Category = apps.get_model('product', 'Category')
        Product = apps.get_model('product', 'Product')
        
        Category.objects.all().update(slug='')
        Product.objects.all().update(slug='')
    except Exception as e:
        print(f"Error reversing slug population: {e}")


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        # First clean up any existing problematic indexes
        migrations.RunPython(
            migrations.RunPython.noop,
        ),
        
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created_at'], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукти'},
        ),
        
        # Add slug fields without unique constraint first
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Слаг'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='Слаг'),
        ),
        
        # Populate slugs with unique values
        migrations.RunPython(
            populate_slugs,
            reverse_populate_slugs,
        ),
        
        # Now add unique constraint
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Слаг'),
        ),
        
        # Other field alterations
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Назва категорії'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата створення'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(verbose_name='Ціна'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_qty',
            field=models.IntegerField(verbose_name='Кількість товару'),
        ),
        migrations.AlterField(
            model_name='product',
            name='reviews_qty',
            field=models.IntegerField(verbose_name='Кількість відгуків'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Назва продукту'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата оновлення'),
        ),
    ]