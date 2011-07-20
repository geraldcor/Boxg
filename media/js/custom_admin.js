django.jQuery(document).ready(function() {
	Array.max = function( array ){
	    return Math.max.apply( Math, array );
	};

	Array.min = function( array ){
	    return Math.min.apply( Math, array );
	};
	
	django.jQuery("input[name*='order']").live("focus", function(){
		old_order = django.jQuery(this).val();
	});
	
	django.jQuery("input[name*='order']").live("change", function(){
		var order = django.jQuery(this);
		if(old_order){
			django.jQuery("input[name*='order']").each(function(){
				var field = django.jQuery(this);
				if(field.val()){
					if(order.attr("id") == field.attr("id")){
						//
					}
					else{
						if(field.val() > old_order){
							if(field.val() <= order.val() && field.val() > old_order){
								field.val(parseInt(field.val())-1);
							}
						}
						else{
							if(field.val() >= order.val() && field.val() < old_order){
								field.val(parseInt(field.val())+1);
							}
						}
					}
				}
			});
		}
	});
	
	django.jQuery("input[type=file]").live("click", function(){
		var all_fields = new Array();
		django.jQuery("input[name*='order']").each(function(){
			if(django.jQuery(this).val()){
				all_fields.push(django.jQuery(this).val());
			}
		});
		next_order = Math.max.apply(null, all_fields) + 1;
		if(!django.jQuery(this).parent().prev().children().val()){
			django.jQuery(this).parent().prev().children().val(next_order)
		}
	});
	
});