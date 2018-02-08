.class public abstract Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;
.super Landroid/support/v4/view/PagerAdapter;
.source "BaseGalleryAdapter.java"

# interfaces
.implements Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView$TransformListener;
.implements Luk/co/senab/photoview/PhotoViewAttacher$OnViewTapListener;
.implements Landroid/view/View$OnLongClickListener;


# instance fields
.field private activity:Landroid/app/Activity;

.field private pager:Landroid/support/v4/view/ViewPager;

.field protected pos:I

.field private taskManager:Lcom/xunmeng/pinduoduo/basekit/thread/infra/DefaultTaskManager;


# direct methods
.method public constructor <init>(Landroid/app/Activity;ILandroid/support/v4/view/ViewPager;)V
    .locals 1
    .param p1, "activity"    # Landroid/app/Activity;
    .param p2, "pos"    # I
    .param p3, "viewPager"    # Landroid/support/v4/view/ViewPager;

    .prologue
    .line 30
    invoke-direct {p0}, Landroid/support/v4/view/PagerAdapter;-><init>()V

    .line 28
    new-instance v0, Lcom/xunmeng/pinduoduo/basekit/thread/infra/DefaultTaskManager;

    invoke-direct {v0}, Lcom/xunmeng/pinduoduo/basekit/thread/infra/DefaultTaskManager;-><init>()V

    iput-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->taskManager:Lcom/xunmeng/pinduoduo/basekit/thread/infra/DefaultTaskManager;

    .line 31
    iput-object p1, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    .line 32
    iput p2, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->pos:I

    .line 33
    iput-object p3, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->pager:Landroid/support/v4/view/ViewPager;

    .line 34
    return-void
.end method

.method static synthetic access$000(Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;)Landroid/support/v4/view/ViewPager;
    .locals 1
    .param p0, "x0"    # Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;

    .prologue
n
    .line 23
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->pager:Landroid/support/v4/view/ViewPager;

    return-object v0
.end method

.method static synthetic access$100(Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;)Lcom/xunmeng/pinduoduo/basekit/thread/infra/DefaultTaskManager;
    .locals 1
    .param p0, "x0"    # Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;

    .prologue
    .line 23
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->taskManager:Lcom/xunmeng/pinduoduo/basekit/thread/infra/DefaultTaskManager;

    return-object v0
.end method


# virtual methods
.method public destroyItem(Landroid/view/ViewGroup;ILjava/lang/Object;)V
    .locals 0
    .param p1, "container"    # Landroid/view/ViewGroup;
    .param p2, "position"    # I
    .param p3, "object"    # Ljava/lang/Object;

    .prologue
    .line 46
    check-cast p3, Landroid/view/View;

    .end local p3    # "object":Ljava/lang/Object;
    invoke-virtual {p1, p3}, Landroid/view/ViewGroup;->removeView(Landroid/view/View;)V

    .line 47
    return-void
.end method

.method protected abstract getImageUri(I)Ljava/lang/String;
.end method

.method protected instantiate(Landroid/view/View;I)V
    .locals 5
    .param p1, "view"    # Landroid/view/View;
    .param p2, "position"    # I

    .prologue
    .line 65
    invoke-virtual {p0, p1}, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->instantiateSmoothImageView(Landroid/view/View;)Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;

    move-result-object v0

    .line 67
    .local v0, "smoothImageView":Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;
    iget-object v1, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    invoke-virtual {p0, p2}, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->getImageUri(I)Ljava/lang/String;

    move-result-object v2

    const/4 v3, 0x0

    const v4, 0x7f020299

    invoke-static {v1, v2, v3, v4, v0}, Lcom/xunmeng/pinduoduo/basekit/image/GlideService;->loadCrossFade(Landroid/content/Context;Ljava/lang/String;IILandroid/widget/ImageView;)V

    .line 68
    invoke-virtual {v0, p0}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;->setOnTransformListener(Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView$TransformListener;)V
  invoke-virtual {v0, p0}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;->addOnTransformListener(Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView$TransformListener;)V


    .line 70
    invoke-virtual {v0, p0}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;->setOnViewTapListener(Luk/co/senab/photoview/PhotoViewAttacher$OnViewTapListener;)V

    .line 72
    invoke-virtual {v0, p0}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;->setOnLongClickListener(Landroid/view/View$OnLongClickListener;)V

    .line 73
    return-void
.end method

.method public instantiateItem(Landroid/view/ViewGroup;I)Ljava/lang/Object;
    .locals 2
    .param p1, "container"    # Landroid/view/ViewGroup;
    .param p2, "position"    # I

    .prologue
    const/4 v1, -0x1

    .line 38
    invoke-virtual {p0, p1, p2}, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->instantiateView(Landroid/view/ViewGroup;I)Landroid/view/View;

    move-result-object v0

    .line 39
    .local v0, "view":Landroid/view/View;
    invoke-virtual {p1, v0, v1, v1}, Landroid/view/ViewGroup;->addView(Landroid/view/View;II)V

    .line 40
    invoke-virtual {p0, v0, p2}, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->instantiate(Landroid/view/View;I)V

    .line 41
    return-object v0
.end method

.method protected instantiateSmoothImageView(Landroid/view/View;)Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;
    .locals 0
    .param p1, "view"    # Landroid/view/View;

    .prologue
    .line 59
    check-cast p1, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;

    .end local p1    # "view":Landroid/view/View;
    return-object p1
.end method

.method protected instantiateView(Landroid/view/ViewGroup;I)Landroid/view/View;
    .locals 3
    .param p1, "container"    # Landroid/view/ViewGroup;
    .param p2, "position"    # I

    .prologue
    .line 55
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    invoke-static {v0}, Landroid/view/LayoutInflater;->from(Landroid/content/Context;)Landroid/view/LayoutInflater;

    move-result-object v0

    const v1, 0x7f040253

    const/4 v2, 0x0

    invoke-virtual {v0, v1, v2}, Landroid/view/LayoutInflater;->inflate(ILandroid/view/ViewGroup;)Landroid/view/View;

    move-result-object v0

    return-object v0
.end method

.method public isViewFromObject(Landroid/view/View;Ljava/lang/Object;)Z
    .locals 1
    .param p1, "view"    # Landroid/view/View;
    .param p2, "object"    # Ljava/lang/Object;

    .prologue
    .line 51
    if-ne p1, p2, :cond_0

    const/4 v0, 0x1

    :goto_0
    return v0

    :cond_0
    const/4 v0, 0x0

    goto :goto_0
.end method

.method public onLongClick(Landroid/view/View;)Z
    .locals 4
    .param p1, "v"    # Landroid/view/View;

    .prologue
    const/4 v3, 0x0

    .line 95
    iget-object v1, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    invoke-virtual {v1}, Landroid/app/Activity;->isFinishing()Z

    move-result v1

    if-eqz v1, :cond_0

    .line 107
    :goto_0
    return v3

    .line 98
    :cond_0
    new-instance v0, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/PictureDialog;

    iget-object v1, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    const v2, 0x7f0b00d0

    invoke-direct {v0, v1, v2}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/PictureDialog;-><init>(Landroid/content/Context;I)V

    .line 99
    .local v0, "dialog":Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/PictureDialog;
    new-instance v1, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter$1;

    invoke-direct {v1, p0, v0}, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter$1;-><init>(Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/PictureDialog;)V

    invoke-virtual {v0, v1}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/PictureDialog;->setOnImageClickListener(Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/PictureDialog$OnImageClickListener;)V

    .line 106
    invoke-virtual {v0}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/PictureDialog;->show()V

    goto :goto_0
.end method

.method public onTransformComplete(I)V
    .locals 2
    .param p1, "mode"    # I

    .prologue
    const/4 v1, 0x0

    .line 77
    const/4 v0, 0x2

    if-ne p1, v0, :cond_0

    .line 78
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    invoke-virtual {v0}, Landroid/app/Activity;->finish()V

    .line 79
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    invoke-virtual {v0, v1, v1}, Landroid/app/Activity;->overridePendingTransition(II)V

    .line 81
    :cond_0
    return-void
.end method

.method public onViewTap(Landroid/view/View;FF)V
    .locals 3
    .param p1, "view"    # Landroid/view/View;
    .param p2, "x"    # F
    .param p3, "y"    # F

    .prologue
    .line 85
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->pager:Landroid/support/v4/view/ViewPager;

    invoke-virtual {v0}, Landroid/support/v4/view/ViewPager;->getCurrentItem()I

    move-result v0

    iget v1, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->pos:I

    if-ne v0, v1, :cond_0

    .line 86
    check-cast p1, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;

    .end local p1    # "view":Landroid/view/View;
    invoke-virtual {p1}, Lcom/xunmeng/pinduoduo/ui/fragment/chat/widget/SmoothImageView;->transformOut()V

    .line 91
    :goto_0
    return-void

    .line 88
    .restart local p1    # "view":Landroid/view/View;
    :cond_0
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    invoke-virtual {v0}, Landroid/app/Activity;->finish()V

    .line 89
    iget-object v0, p0, Lcom/xunmeng/pinduoduo/adapter/BaseGalleryAdapter;->activity:Landroid/app/Activity;

    const v1, 0x7f05000e

    const v2, 0x7f05000f

    invoke-virtual {v0, v1, v2}, Landroid/app/Activity;->overridePendingTransition(II)V

    goto :goto_0
.end method
